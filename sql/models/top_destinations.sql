-- Query to get the top 5 most booked destinations
SELECT destination, COUNT(*) AS booking_count
FROM travel_bookings
GROUP BY destination
ORDER BY booking_count DESC
LIMIT 5;
