import os
import pandas as pd

PROCESSED_FOLDER = "data/processed/"
PORTFOLIO_FOLDER = "portfolio_outputs/"

# Ensure portfolio folder exists
os.makedirs(PORTFOLIO_FOLDER, exist_ok=True)

# Get latest processed CSV
processed_files = [f for f in os.listdir(PROCESSED_FOLDER) if f.endswith(".csv")]

if not processed_files:
    print("No processed CSV files found.")
    exit()

latest_file = max(processed_files, key=lambda f: os.path.getctime(os.path.join(PROCESSED_FOLDER, f)))
processed_csv = os.path.join(PROCESSED_FOLDER, latest_file)

print(f"Generating portfolio outputs from: {processed_csv}")

# Read processed data
df = pd.read_csv(processed_csv)

# ----------------------------
# Top Destinations
# ----------------------------
top_dest = df.groupby('destination')['booking_id'].count().reset_index()
top_dest.rename(columns={'booking_id': 'total_bookings'}, inplace=True)

top_dest.to_csv(os.path.join(PORTFOLIO_FOLDER, "top_destinations_summary.csv"), index=False)

# ----------------------------
# Bookings Per Month
# ----------------------------
df['booking_month'] = pd.to_datetime(df['booking_date']).dt.to_period('M')

monthly = df.groupby('booking_month')['booking_id'].count().reset_index()
monthly.rename(columns={'booking_id': 'total_bookings'}, inplace=True)

monthly.to_csv(os.path.join(PORTFOLIO_FOLDER, "bookings_per_month_summary.csv"), index=False)

# ----------------------------
# Revenue Per Destination (USD standardized)
# ----------------------------
revenue = df.groupby('destination')['price'].sum().reset_index()
revenue.rename(columns={'price': 'total_revenue_usd'}, inplace=True)

revenue.to_csv(os.path.join(PORTFOLIO_FOLDER, "revenue_per_destination.csv"), index=False)

# ----------------------------
# Booking Status Summary
# ----------------------------
status = df.groupby('booking_status')['booking_id'].count().reset_index()
status.rename(columns={'booking_id': 'total_bookings'}, inplace=True)

status.to_csv(os.path.join(PORTFOLIO_FOLDER, "booking_status_summary.csv"), index=False)

print("Portfolio outputs successfully generated in portfolio_outputs/ folder.")
