-- Count of bookings by status
SELECT booking_status, COUNT(*) AS total
FROM travel_bookings
GROUP BY booking_status;
