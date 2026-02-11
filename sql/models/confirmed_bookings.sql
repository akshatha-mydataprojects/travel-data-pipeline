-- Query to get all confirmed bookings
SELECT *
FROM travel_bookings
WHERE booking_status = 'confirmed';
