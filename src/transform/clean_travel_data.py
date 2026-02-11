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

    logging.info("Data transformation completed")

    return df
