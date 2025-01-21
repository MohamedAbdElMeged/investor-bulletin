""" Rule Service"""
"""_summary_
this file to write any business logic for the Rules
"""
from .alert_dal import AlertCreate
from .alert_dal import get_all_alerts_dal, create_alert_dal


def get_all_alerts(session):
    return get_all_alerts_dal(session)

def create_new_alert( alert: AlertCreate, session ):
    return create_alert_dal(alert=alert, session=session)