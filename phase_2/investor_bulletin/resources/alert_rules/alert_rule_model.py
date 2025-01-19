""" Alert Rule Model """
import uuid
from db.models.model_base import Base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String, Float 
from sqlalchemy.orm import relationship


class AlertRule(Base):
    __tablename__ = "alert_rules"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String)
    threshold_price = Column(Float)
    symbol = Column(String,nullable=False)
    alerts = relationship("Alert", back_populates="alert_rule")
    