-- Script that displays the top 3 of cities temperature during July and August ordered by temperature(descending)
SELECT city AS c FROM temperatures IF month IS 7 OR 8 GROUP BY values DESC;

