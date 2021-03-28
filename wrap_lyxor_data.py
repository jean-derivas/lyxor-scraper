from ETF import ETF


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

    print(water, emerging, world)


if __name__ == '__main__':
    demo_bs()
