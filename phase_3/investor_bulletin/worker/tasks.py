
from worker.celery_app import celery_app
from resources.market.market_service import get_market_data
from core.messaging import publish_message
from common.stock_symbols import StockSymbols
from resources.market.market_schema import MarketPriceResponse

@celery_app.task
def get_market_prices_and_check_alert_rules():
    symbols = [symbol.value for symbol in StockSymbols]
    market_stock_prices = get_market_data(symbols)
    for market_stock_price in market_stock_prices:
        if market_stock_price is not None:
            publish_message(format_market_stock_price(market_stock_price))
    return "market_stock_price"


def format_market_stock_price(market_stock_price: MarketPriceResponse):
    return {
        "event": "THRESHOLD_ALERT",
        "symbol": market_stock_price.symbol,
        "price": market_stock_price.price
    }