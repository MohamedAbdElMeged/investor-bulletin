""" Market Service """
"""_summary_
this file to write any business logic for the Market
"""


import os
import requests
from typing import List
from dotenv import load_dotenv
from resources.market.market_schema import MarketPriceResponse

load_dotenv()

def get_market_data(symbols: List[str]):
    market_stock_prices = []
    for symbol in symbols:
        market_stock_price = get_stock_price_for_symbol(symbol)
        market_stock_prices.append(market_stock_price)
    return market_stock_prices


def get_stock_price_for_symbol(symbol: str):
    try:
        api_url = os.environ["MARKET_API_URL"]
        api_key = os.environ["MARKET_API_KEY"]
        params = {
            "symbol": symbol
        }
        headers = {
            "Authorization": "apikey " + api_key
        }
        response = requests.get(api_url,params=params,headers=headers)
        
        if response.status_code == 200:
            json_response = response.json()
            response_price = float(json_response["price"])
            
            return MarketPriceResponse(symbol=symbol,price= response_price)
    except:
        return
