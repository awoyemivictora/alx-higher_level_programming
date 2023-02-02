-- Script that lists the number of records with the same score in the table second_table
SELECT score, COUNT(*) as c FROM some_table ORDER BY score;

