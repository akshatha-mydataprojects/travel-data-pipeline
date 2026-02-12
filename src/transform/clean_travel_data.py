import pandas as pd
import logging

def clean_data(df):
    logging.info("Starting data transformation")

    # Remove duplicates
    df = df.drop_duplicates()

    # Remove rows with missing critical fields
    df = df.dropna(subset=['booking_id', 'user_id', 'price'])

    # Standardize text columns
    df['destination'] = df['destination'].str.title()
    df['booking_status'] = df['booking_status'].str.lower()

    # Convert dates
    df['booking_date'] = pd.to_datetime(df['booking_date'])
    df['travel_date'] = pd.to_datetime(df['travel_date'])

    # Ensure numeric type
    df['price'] = pd.to_numeric(df['price'], errors='coerce')
    
    # Standardize prices to USD
    exchange_rates = {
        'USD': 1,
        'EUR': 1.1,  # 1 EUR = 1.1 USD
        'GBP': 1.3   # 1 GBP = 1.3 USD
    }

    # Create a new column for standardized price
    df['price_usd'] = df.apply(lambda row: round(row['price'] * exchange_rates.get(row['currency'], 1), 2), axis=1)

    # Overwrite price with USD and currency column
    df['price'] = df['price_usd']
    df['currency'] = 'USD'
    df.drop(columns=['price_usd'], inplace=True)


    logging.info("Data transformation completed")

    return df
