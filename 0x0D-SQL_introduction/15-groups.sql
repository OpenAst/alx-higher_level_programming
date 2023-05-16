--- lists the number of records with the same score in the table
---in the second_table
---sorted by number of records
---display the score
SELECT score, COUNT('score') as number
FROM second_table
GROUP BY score
ORDER BY score DESC;
