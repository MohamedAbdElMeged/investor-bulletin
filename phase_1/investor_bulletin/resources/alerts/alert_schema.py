""" Alert Schema """
"""_summary_
This file to abstract any validation logic for the Alerts
"""
from resources.alert_rules.alert_rule_model import AlertRule
from pydantic import BaseModel

class AlertCreate(BaseModel):
    symbol: str
    stock_price: float
    alert_rule: AlertRule