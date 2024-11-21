# Write your MySQL query statement below
SELECT c.id, c.movie, c.description, c.rating from Cinema c
WHERE (c.id % 2 != 0) AND (c.description != 'boring')
ORDER BY rating desc;