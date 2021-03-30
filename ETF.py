import pandas as pd
import requests
from bs4 import BeautifulSoup


class ETF(object):
    top_ten: pd.DataFrame
    sector: pd.DataFrame
    currency: pd.DataFrame
    country: pd.DataFrame
    name: str

    def __init__(self, url, name):
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET',
            'Access-Control-Allow-Headers': 'Content-Type',
        }

        req = requests.get(url, headers)
        soup = BeautifulSoup(req.content, 'html.parser')

        self.name = name
        self.top_ten = self._extract_table(soup, "topTenIndex")
        self.sector = self._load_sector(soup, name)
        self.currency = self._load_currency(soup, name)
        self.country = self._load_country(soup, name)

    @staticmethod
    def _load_currency(soup, name):
        df = ETF._extract_table(soup, "breakdown-scrollable-box-index-currencies")
        df = df.drop(2, axis=1)
        df.columns = ["Currency", name]
        df = df.set_index("Currency")
        df = df.replace(regex=r'%', value="")
        df = df.replace(regex=r',', value=".")
        df[name] = pd.to_numeric(df[name])
        return df

    @staticmethod
    def _load_sector(soup, name):
        df = ETF._extract_table(soup, "breakdown-scrollable-box-index-sectors")
        df = df.drop(2, axis=1)
        df.columns = ["Sector", name]
        df = df.set_index("Sector")
        df = df.replace(regex=r'%', value="")
        df = df.replace(regex=r',', value=".")
        df[name] = pd.to_numeric(df[name])
        return df

    @staticmethod
    def _load_country(soup, name):
        df = ETF._extract_table(soup, "breakdown-scrollable-box-index-countries")
        df.columns = ["Country", name]
        df = df.set_index("Country")
        df = df.replace(regex=r'%', value="")
        df = df.replace(regex=r',', value=".")
        df[name] = pd.to_numeric(df[name])
        return df

    @staticmethod
    def _extract_table(soup, index) -> pd.DataFrame:
        div = soup.find_all("div", {"id": ("%s" % index)})
        if len(div) == 1:
            df_div = pd.read_html(str(div[0]))
        else:
            raise RuntimeError("extract table failed. Table not found or more than one.")
        return df_div[0]
