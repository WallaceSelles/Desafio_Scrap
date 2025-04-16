
import requests
from bs4 import BeautifulSoup
import pandas as pd

class CoinMarketCapScraper:
    def fetch_data(self):
        url = "https://coinmarketcap.com/"
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(response.text, "html.parser")

        coins = []
        rows = soup.select("table tbody tr")[:10]

        for row in rows:
            cols = row.find_all("td")
            if len(cols) >= 7:
                name = cols[2].find("p").text
                symbol = cols[2].find_all("p")[1].text
                price = cols[3].text
                market_cap = cols[7].text
                volume = cols[6].text
                change = cols[4].text
                coins.append({
                    "Name": name,
                    "Symbol": symbol,
                    "Price": price,
                    "Market Cap": market_cap,
                    "24h Volume": volume,
                    "Change (24h)": change
                })

        return pd.DataFrame(coins)
