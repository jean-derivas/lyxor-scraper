from ETF import ETF
from scipy import optimize

def demo_bs():
    world = ETF(
        "https://www.lyxoretf.fr/fr/retail/produits/etf-actions/lyxor-msci-world-ucits-etf-dist/fr0010315770/eur",
        "world")

    water = ETF(
        "https://www.lyxoretf.fr/fr/retail/produits/etf-actions/lyxor-world-water-dr-ucits-etf-dist/fr0010527275/eur",
        "water")

    emerging = ETF(
        "https://www.lyxoretf.fr/fr/retail/produits/etf-actions/lyxor-msci-emerging-markets-ucits-etf-acc-eur/fr0010429068/eur",
        "emerging")

    country = world.country.join(water.country, how="outer").join(emerging.country, how="outer")
    country.fillna("0", inplace=True)
    country = country.astype("float64")

    currency = world.currency.join(water.currency).join(emerging.currency)
    currency.fillna("0", inplace=True)
    currency = currency.astype("float64")

    sector = world.sector.join(water.sector).join(emerging.sector)
    sector.fillna("0", inplace=True)
    sector = sector.astype("float64")

    optimize.minimize()

    print("end")


if __name__ == '__main__':
    demo_bs()
