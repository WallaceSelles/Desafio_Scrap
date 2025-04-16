
from scraping.services.scraper import CoinMarketCapScraper
from scraping.data.writer import CSVWriter

if __name__ == "__main__":
    scraper = CoinMarketCapScraper()
    data = scraper.fetch_data()

    writer = CSVWriter("output/coins_scraping.csv")
    writer.write(data)
