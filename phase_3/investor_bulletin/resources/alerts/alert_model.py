""" Alert Model """
import uuid
from datetime import datetime
from db.models.model_base import Base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, ForeignKey, DateTime, Float, String
from sqlalchemy.orm import relationship

class Alert(Base):
    __tablename__ = 'alerts'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    alert_rule_id = Column(UUID(as_uuid=True), ForeignKey("alert_rules.id"), nullable=False)
    triggered_at = Column(DateTime, default=datetime.now())  
    stock_price = Column(Float, nullable=False)  
    symbol = Column(String,nullable=False)
    alert_rule = relationship("AlertRule", back_populates="alerts")