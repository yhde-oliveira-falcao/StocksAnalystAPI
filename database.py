from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Initial engine for creating the DB
INIT_ENGINE = create_engine("mysql+pymysql://root:Program_Coffee_123@localhost", isolation_level="AUTOCOMMIT")

with INIT_ENGINE.connect() as conn:
    conn.execute(text("CREATE DATABASE IF NOT EXISTS StockData"))

# Main engine connected to the actual DB
DATABASE_URL = "mysql+pymysql://root:Program_Coffee_123@localhost/StockData"
engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()