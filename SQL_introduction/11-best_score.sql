-- List score and name from second_list in descending score order where score is >= 10.
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
