import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from resources.alert_rules.alert_rule_model import AlertRule
from resources.alerts.alert_model import Alert



from dotenv import load_dotenv
from .model_base import Base


load_dotenv()



# Updated Database URL for CockroachDB
DATABASE_URL = os.environ["DATABASE_URL"]

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create a configured "Session" class
SessionLocal = sessionmaker(bind=engine)

# Base class for models
Base.metadata.create_all(engine)

session = SessionLocal()