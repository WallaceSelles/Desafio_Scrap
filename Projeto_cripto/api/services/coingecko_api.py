
import requests
import pandas as pd

class CoinGeckoClient:
    def fetch_data(self):
        url = "https://api.coingecko.com/api/v3/coins/markets"
        params = {
            "vs_currency": "usd",
            "order": "market_cap_desc",
            "per_page": 10,
            "page": 1,
            "sparkline": False
        }
        response = requests.get(url, params=params)
        data = response.json()

        coins = []
        for coin in data:
            coins.append({
                "Name": coin["name"],
                "Symbol": coin["symbol"].upper(),
                "Price": coin["current_price"],
                "Market Cap": coin["market_cap"],
                "24h Volume": coin["total_volume"],
                "Change (24h)": coin["price_change_percentage_24h"]
            })

        return pd.DataFrame(coins)
