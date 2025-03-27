from data_loader import load_data, preprocess_data
from database import save_to_db

def main():
    # Загрузка и предобработка данных
    symbol = "EURUSD=X"
    start_date = "2025-02-01"
    end_date = "2025-03-01"
    
    data = load_data(symbol, start_date, end_date)
    processed_data = preprocess_data(data)
    
    # Сохранение в базу данных
    save_to_db(processed_data)

if __name__ == "__main__":
    main()
