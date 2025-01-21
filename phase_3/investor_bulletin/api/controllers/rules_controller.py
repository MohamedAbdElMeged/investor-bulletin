from fastapi import APIRouter
from resources.alert_rules.alert_rule_schema import AlertRuleCreate, AlertRuleUpdate
from resources.alert_rules.alert_rule_service import create_alert_rule, update_alert_rule, get_all_alert_rules,delete_alert_rule
from resources.alerts.alert_service import get_all_alerts
from db.models.models import session,SessionLocal
router = APIRouter()

@router.post("")
def create(alert_rule: AlertRuleCreate):
    alert_rule = create_alert_rule(alert_rule, session)
    return alert_rule


@router.patch("/{id}") 
def update(id: str,new_rule: AlertRuleUpdate):

    return update_alert_rule(id,new_rule, session)


@router.get("")
def get_all_rules():
    return get_all_alert_rules(session)


@router.delete("/{id}")
def delete(id:str):
    return delete_alert_rule(id, session)

@router.get("/alerts")
def get_alerts():
    return get_all_alerts(SessionLocal)
