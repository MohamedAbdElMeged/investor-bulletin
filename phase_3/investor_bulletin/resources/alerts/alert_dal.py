""" Alert DAL"""
"""_summary_
this file is to right any ORM logic for the Alert model
"""
from .alert_schema import AlertCreate
from db.models import Alert
from datetime import datetime
def create_alert_dal( alert: AlertCreate, session ):
    new_alert = None
    with session() as sess:
        new_alert = Alert(symbol=alert.symbol,stock_price=alert.stock_price,alert_rule_id=alert.alert_rule_id)
        sess.add(new_alert)
        sess.commit()
        sess.refresh(new_alert)
    return new_alert


def get_all_alerts_dal(session):
    with session() as sess:
        return sess.query(Alert).all()