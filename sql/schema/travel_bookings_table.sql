-- Create the main travel bookings table
CREATE TABLE IF NOT EXISTS travel_bookings (
        booking_id INT PRIMARY KEY,
        user_id INT,
        destination VARCHAR(100),
        booking_date DATE,
        travel_date DATE,
        price NUMERIC,
        currency VARCHAR(10),
        booking_status VARCHAR(20)
);
