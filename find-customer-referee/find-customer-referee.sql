# Write your MySQL query statement below
/*
Table: Customer

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| referee_id  | int 
*/

SELECT
    name
FROM 
    Customer
WHERE
    (referee_id != 2) 
        OR 
    (referee_id IS NULL)