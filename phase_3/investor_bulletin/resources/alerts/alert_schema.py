""" Alert Schema """
"""_summary_
This file to abstract any validation logic for the Alerts
"""
from datetime import datetime
from pydantic import BaseModel
from uuid import UUID

class AlertCreate(BaseModel):
    symbol: str
    stock_price: float
    alert_rule_id: UUID
    triggered_at: datetime