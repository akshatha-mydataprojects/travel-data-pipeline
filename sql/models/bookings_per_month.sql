-- Query to count bookings per month
SELECT 
    DATE_TRUNC('month', booking_date) AS booking_month,
    COUNT(*) AS total_bookings
FROM travel_bookings
GROUP BY booking_month
ORDER BY booking_month;
