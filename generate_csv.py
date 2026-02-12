import pandas as pd
import random
from datetime import datetime, timedelta
import os

# Number of rows
N = 200

# Destinations, statuses, currencies
destinations = ['Miami', 'Washington', 'New York', 'Los Angeles', 'Chicago', 'Seattle']
statuses = ['confirmed', 'cancelled', 'pending']
currencies = ['USD', 'EUR', 'GBP']

start_date = datetime(2025, 1, 1)
data = []

for i in range(1, N+1):
    booking_id = i
    user_id = random.randint(1000, 9999)
    destination = random.choice(destinations)
    booking_date = start_date + timedelta(days=random.randint(0, 365))
    travel_date = booking_date + timedelta(days=random.randint(1, 60))
    price = round(random.uniform(100, 2000), 2)
    currency = random.choice(currencies)
    booking_status = random.choice(statuses)

    data.append([booking_id, user_id, destination, booking_date.date(), travel_date.date(), price, currency, booking_status])

df = pd.DataFrame(data, columns=[
    'booking_id', 'user_id', 'destination', 'booking_date', 'travel_date', 'price', 'currency', 'booking_status'
])

# Ensure raw folder exists
os.makedirs("data/raw", exist_ok=True)

# Save CSV
output_path = "data/raw/large_travel_bookings.csv"
df.to_csv(output_path, index=False)
print(f"Large sample CSV created with {N} rows at {output_path}!")
