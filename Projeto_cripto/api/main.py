
from api.services.coingecko_api import CoinGeckoClient
from api.data.writer import CSVWriter

if __name__ == "__main__":
    client = CoinGeckoClient()
    data = client.fetch_data()

    writer = CSVWriter("output/coins_api.csv")
    writer.write(data)
