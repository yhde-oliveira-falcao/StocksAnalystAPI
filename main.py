from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from sqlalchemy.orm import Session
from sqlalchemy import func
from database import engine, SessionLocal
from models import StockDaily
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


templates = Jinja2Templates(directory="templates")

@app.post("/fetch_stock_data/{ticker}")
def fetch_stock_data_route(
    ticker: str,
    from_date: str = None,
    to_date: str = None,
    db: Session = Depends(get_db)
):
    fetch_and_save_stock_data(ticker, db, from_date, to_date)
    return {"message": f"Stock data for {ticker} fetched and saved."}

@app.get("/stocks/summary")
def get_stocks_summary(db: Session = Depends(get_db)):
    results = (
        db.query(
            StockDaily.ticker,
            func.min(StockDaily.date).label("start_date"),
            func.max(StockDaily.date).label("end_date")
        )
        .group_by(StockDaily.ticker)
        .all()
    )
    summaries = [
        {"ticker": ticker, "start_date": start_date.isoformat(), "end_date": end_date.isoformat()}
        for ticker, start_date, end_date in results
    ]
    return JSONResponse(content=summaries)

@app.get("/stocks/html_summary")
def get_stocks_html_summary(request: Request, db: Session = Depends(get_db)):
    results = (
        db.query(
            StockDaily.ticker,
            func.min(StockDaily.date).label("start_date"),
            func.max(StockDaily.date).label("end_date")
        )
        .group_by(StockDaily.ticker)
        .all()
    )

    summaries = [
        {"ticker": ticker, "start_date": start_date.isoformat(), "end_date": end_date.isoformat()}
        for ticker, start_date, end_date in results
    ]

    return templates.TemplateResponse("stocks_summary.html", {"request": request, "stocks": summaries})



