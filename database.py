from sqlalchemy import create_engine, Column, Integer, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pandas as pd

DATABASE_URL = "postgresql://postgres:nirvana@localhost:5432/traiding_database"
Base = declarative_base()

class HistoricalData(Base):
    __tablename__ = 'historical_data'
    id = Column(Integer, primary_key=True)
    datetime = Column(DateTime)
    open = Column(Float)
    high = Column(Float)
    low = Column(Float)
    close = Column(Float)

# Создание подключения к БД
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

def save_to_db(data: pd.DataFrame):
    """
    Сохраняет данные в базу данных PostgreSQL.
    
    :param data: DataFrame с данными для сохранения
    """
    session = Session()
    
    for index, row in data.iterrows():
        record = HistoricalData(
            datetime=pd.to_datetime(row.name),
            open=float(row['Open']),
            high=float(row['High']),
            low=float(row['Low']),
            close=float(row['Close'])
        )
        session.add(record)
    
    session.commit()
    session.close()