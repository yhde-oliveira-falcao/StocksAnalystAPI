from sqlalchemy import Boolean, Column, Integer, String, Date, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class StockDaily(Base):
    __tablename__ = 'stocks_daily'

    id = Column(Integer, primary_key=True, index=True)
    ticker = Column(String(10), index=True)
    date = Column(Date, index=True)
    open = Column(Float)
    high = Column(Float)
    low = Column(Float)
    close = Column(Float)
    volume = Column(Integer)

    # Optional: establish backref if you plan to link dividends to daily data
    dividends = relationship("Dividend", back_populates="stock", cascade="all, delete-orphan")


class Dividend(Base):
    __tablename__ = 'dividends'

    id = Column(Integer, primary_key=True, autoincrement=True)
    ex_date = Column(String(20))
    amount = Column(Float, nullable=False)
    declaration = Column(String(100))
    record_date = Column(String(20))
    pay_date = Column(String(20))

    stock_id = Column(Integer, ForeignKey('stocks_daily.id'), nullable=False)
    stock = relationship("StockDaily", back_populates="dividends")
