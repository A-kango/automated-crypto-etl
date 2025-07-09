# etl_crypto_pipeline.py

import requests
import pandas as pd
from sqlalchemy import create_engine
import json
import pyodbc
from datetime import datetime

def extract_data():
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def transform_data(raw_data):
    df = pd.DataFrame(data=raw_data)
    df.set_index('name', inplace=True)

    # Reorder columns
    cols = df.columns.tolist()
    cols.remove('id')
    cols.remove('symbol')
    new_order = ['id', 'symbol'] + cols
    df = df[new_order]

    # Handle nulls, format timestamps, filter unnecessary columns
    df.fillna(0, inplace=True)
    df.drop(columns=['image'], inplace=True)
    df['last_updated'] = pd.to_datetime(df['last_updated']).dt.strftime('%d-%b-%Y %I:%M %p')
    df['market_cap_change_percentage_24h'] = df['market_cap_change_percentage_24h'].abs()

    if 'roi' in df.columns:
        df['roi'] = df['roi'].apply(lambda x: json.dumps(x) if isinstance(x, dict) else x)

    return df

def load_to_postgresql(df):
    engine = create_engine("postgresql://postgres:Anthony8700@localhost:5432/Crytocurrency_wahehouse")
    df.to_sql("crypto_market_data", engine, if_exists='replace', index=True)
    print("✅ Data successfully loaded into PostgreSQL table 'crypto_market_data'")

def preview_data_with_pyodbc():
    conn_str = (
        "DRIVER={Devart ODBC Driver for PostgreSQL};"
        "Server=localhost;"
        "Port=5432;"
        "Database=Crytocurrency_wahehouse;"
        "User ID=postgres;"
        "Password=Anthony8700"
    )

    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()

    cursor.execute("SELECT name, current_price FROM crypto_market_data LIMIT 5")
    for row in cursor.fetchall():
        print(row)

    conn.close()

if __name__ == "__main__":
    print(f"🔄 ETL Pipeline Started at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    raw_data = extract_data()
    transformed_data = transform_data(raw_data)
    load_to_postgresql(transformed_data)
    preview_data_with_pyodbc()

    print(f"✅ ETL Pipeline Completed at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")


