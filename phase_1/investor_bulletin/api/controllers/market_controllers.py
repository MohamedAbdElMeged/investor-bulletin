import requests
from typing import List
from fastapi import APIRouter, HTTPException, Query
from investor_bulletin.common.stock_symbols import StockSymbols
from investor_bulletin.resources.market.market_schema import MarketPriceResponse

from investor_bulletin.resources.market.market_service import get_market_data

router = APIRouter()

@router.get("")
def get_market_data_route(symbols: List[StockSymbols]=  Query(None)):
    # validate that symbols must be sent and its length must be greater than 0
    if symbols is None or len(symbols) == 0:
        raise HTTPException(status_code=400, detail="Please Provide Symbols")
    symbols_values = []
    for symbol in symbols:
        symbols_values.append(symbol.value) 
    return get_market_data(symbols_values)
