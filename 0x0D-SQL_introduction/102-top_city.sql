-- Displays the average temperature (in Fahrenheit)
-- by city ordered by descending temperature.
SELECT city, AVG(value) AS avg_tem
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
