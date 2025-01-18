""" Alert Rule  DAL"""
"""_summary_
this file is to right any ORM logic for the Alert Rule model
"""
from resources.alert_rules.alert_rule_schema import AlertRuleCreate, AlertRuleUpdate
from db.models import AlertRule
from fastapi import HTTPException


def create_alert_rule_dal( rule: AlertRuleCreate, session ):
    new_rule = AlertRule(name=rule.name,threshold_price=rule.threshold,symbol=rule.symbol.value)
    session.add(new_rule)
    session.commit()
    session.refresh(new_rule)
    return new_rule

def update_alert_rule_dal(id: str, new_rule: AlertRuleUpdate, session):
    alert_rule = get_alert_rule_dal(id,session)
    if not alert_rule:
        raise HTTPException(status_code=404, detail="Alert Rule not found")
    if new_rule.name:
        alert_rule.name = new_rule.name
    if new_rule.symbol:
        alert_rule.symbol = new_rule.symbol.value
    if new_rule.threshold:
        alert_rule.threshold_price = new_rule.threshold

    session.commit()
    session.refresh(alert_rule)
    return alert_rule


def get_all_alert_rules_dal(session):
    return session.query(AlertRule).all()

def get_alert_rule_dal(id: str, session):
    return session.query(AlertRule).get(id)

def delete_alert_rule_dal(id: str, session):
    alert_rule = get_alert_rule_dal(id,session)
    if not alert_rule:
        raise HTTPException(status_code=404, detail="Alert Rule not found")
    session.delete(alert_rule)
    session.commit()
    return {"message": "Deleted Successfully"}