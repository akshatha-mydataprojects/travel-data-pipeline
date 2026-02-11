-- Calculate total revenue per destination
SELECT 
    destination,
    SUM(price) AS total_revenue
FROM travel_bookings
GROUP BY destination
ORDER BY total_revenue DESC;
