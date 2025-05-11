from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import engine, SessionLocal
import models
from api_requests import fetch_and_save_stock_data

app = FastAPI()

# Create tables AFTER ensuring DB exists
models.Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/fetch_stock_data/{ticker}")
def fetch_stock_data_route(
    ticker: str,
    from_date: str = None,
    to_date: str = None,
    db: Session = Depends(get_db)
):
    fetch_and_save_stock_data(ticker, db, from_date, to_date)
    return {"message": f"Stock data for {ticker} fetched and saved."}
