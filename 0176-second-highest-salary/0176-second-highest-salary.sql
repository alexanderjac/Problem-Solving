# Write your MySQL query statement below
# select max(salary) as SecondHighestSalary  from employee
# where salary < (select max(salary) from employee)
# with cte as (
# select salary, rank() over (order by salary desc ) as rankNo from employee   )

# select  max(salary) as SecondHighestSalary from cte where rankNo = 2

WITH CTE AS
			(SELECT Salary, DENSE_RANK() OVER (ORDER BY Salary desc) AS RANK_desc
			   FROM Employee)
SELECT max(salary) AS SecondHighestSalary
  FROM CTE
 WHERE RANK_desc = 2