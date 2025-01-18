""" Alert Rule Schema """
"""_summary_
This file to abstract any validation logic for the Alert Rules
"""
from investor_bulletin.common.stock_symbols import StockSymbols
from pydantic import BaseModel

class AlertRuleCreate(BaseModel):
    symbol: StockSymbols
    name: str
    threshold: float

class AlertRuleUpdate(BaseModel):
    # use None - None to make all parameters optional
    symbol: str | None = None
    name: str | None = None
    threshold: float | None = None

