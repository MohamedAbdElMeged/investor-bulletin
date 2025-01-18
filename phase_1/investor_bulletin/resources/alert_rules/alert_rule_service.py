""" Alert Rule Service"""
"""_summary_
this file to write any business logic for the Alert Rules
"""
from resources.alert_rules.alert_rule_schema import AlertRuleCreate, AlertRuleUpdate
from resources.alert_rules.alert_rule_dal import create_alert_rule_dal, update_alert_rule_dal,get_all_alert_rules_dal,delete_alert_rule_dal 

def create_alert_rule( rule: AlertRuleCreate, session ):
    return create_alert_rule_dal( rule=rule, session=session)

def update_alert_rule(id: str, new_rule: AlertRuleUpdate, session):
    return update_alert_rule_dal(id,new_rule, session)


def get_all_alert_rules(session):
    return get_all_alert_rules_dal(session)
    
def delete_alert_rule(id: str, session):
    return delete_alert_rule_dal(id,session)