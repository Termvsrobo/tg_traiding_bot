import yfinance as yf
import pandas as pd

def load_data(symbol: str, start_date: str, end_date: str, interval: str = '30m'):
    """
    Загружает данные с yfinance для указанного символа за указанный диапазон дат и интервал.
    
    :param symbol: символ актива (например, 'EURUSD=X' для евро/доллара)
    :param start_date: начальная дата (в формате 'YYYY-MM-DD')
    :param end_date: конечная дата (в формате 'YYYY-MM-DD')
    :param interval: интервал свечей ('30m', '1h', '1d' и т. д.)
    :return: DataFrame с историческими данными
    """
    data = yf.download(symbol, start=start_date, end=end_date, interval=interval)
    return data

def preprocess_data(data: pd.DataFrame):
    """
    Обрабатывает данные: проверяет на пропуски и заполняет их, если нужно.
    
    :param data: DataFrame с историческими данными
    :return: DataFrame с обработанными данными
    """
    if data.isnull().values.any():
        print("Найдены пропуски в данных. Заполняем пропуски...")
        data = data.fillna(method='ffill')  # Заполнение пропусков методом forward fill
    
    return data