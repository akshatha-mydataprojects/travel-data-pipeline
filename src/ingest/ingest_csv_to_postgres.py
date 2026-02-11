import pandas as pd
import psycopg2
from psycopg2 import sql
import logging
from datetime import datetime
from src.utils.db_connection import get_connection
from src.transform.clean_travel_data import clean_data

# 1️⃣ Setup logging
log_filename = f"logs/etl_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
logging.basicConfig(
    filename=log_filename,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# 2️⃣ Define CSV and target table
csv_file = "data/raw/travel_bookings.csv"
table_name = "travel_bookings"

try:
    # 3️⃣ Load and clean CSV
    df_raw = pd.read_csv(csv_file)
    logging.info(f"Raw CSV loaded with {len(df_raw)} rows")

    df = clean_data(df_raw)
    logging.info(f"Cleaned data has {len(df)} rows")

#  Save cleaned data
    processed_file = "data/processed/cleaned_travel_bookings.csv"
    df.to_csv(processed_file, index=False)
    logging.info(f"Cleaned data saved to {processed_file}")


    # 4️⃣ Simple Validation
    required_columns = ['booking_id','user_id','destination','booking_date','travel_date','price','currency','booking_status']
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")

    logging.info("CSV validation passed")

    # 5️⃣ Connect to PostgreSQL
    conn = get_connection()
    cursor = conn.cursor()

    # 6️⃣ Create table if not exists
    create_table_query = f"""
    CREATE TABLE IF NOT EXISTS {table_name} (
        booking_id INT PRIMARY KEY,
        user_id INT,
        destination VARCHAR(100),
        booking_date DATE,
        travel_date DATE,
        price NUMERIC,
        currency VARCHAR(10),
        booking_status VARCHAR(20)
    );
    """
    cursor.execute(create_table_query)
    conn.commit()
    logging.info(f"Table '{table_name}' checked/created successfully")

    # 7️⃣ Insert CSV rows
    for _, row in df.iterrows():
        insert_query = sql.SQL(
            "INSERT INTO {} (booking_id,user_id,destination,booking_date,travel_date,price,currency,booking_status) "
            "VALUES (%s,%s,%s,%s,%s,%s,%s,%s) ON CONFLICT (booking_id) DO NOTHING"
        ).format(sql.Identifier(table_name))

        cursor.execute(insert_query, tuple(row))
    conn.commit()
    logging.info(f"{len(df)} rows inserted successfully into '{table_name}'")

    cursor.close()
    conn.close()
    logging.info("Database connection closed")

except Exception as e:
    logging.error(f"ETL failed: {e}")
    print(f"❌ ETL failed: {e}")
else:
    print(f"✅ ETL completed successfully, check logs: {log_filename}")
