""" Alert DAL"""
"""_summary_
this file is to right any ORM logic for the Alert model
"""
# from resources.alerts.alert_schema import AlertCreate
from db.models import Alert

# def create_rule( rule: AlertCreate, session ):
#     new_alert = Alert()
#     session.add(new_alert)


def get_all_alerts_dal(session):
    return session.query(Alert).all()