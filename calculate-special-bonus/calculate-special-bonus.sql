# Write your MySQL query statement below
/*
Table: Employees

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| employee_id | int     |
| name        | varchar |
| salary      | int     |
+-------------+---------+ 
Write a solution to calculate the bonus of each employee. The bonus of an employee is 100% of their salary if the ID of the employee is an odd number and the employee's name does not start with the character 'M'. The bonus of an employee is 0 otherwise.

Return the result table ordered by employee_id.
*/
SELECT 
    employee_id,
    IF(employee_id % 2 = 1 AND name NOT REGEXP '^M', salary, 0) AS bonus 
FROM 
    employees 
ORDER BY 
    employee_id