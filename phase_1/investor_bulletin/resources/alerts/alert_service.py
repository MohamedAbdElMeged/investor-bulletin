""" Rule Service"""
"""_summary_
this file to write any business logic for the Rules
"""
# from resources.alerts.alerts_schema import AlertCreate
# from resources.alerts.alert_dal import create_alert

# def create_new_alert( rule: AlertCreate, session ):
#     return create_rule( rule=rule, session=session)



from resources.alerts.alert_dal import get_all_alerts_dal


def get_all_alerts(session):
    return get_all_alerts_dal(session)