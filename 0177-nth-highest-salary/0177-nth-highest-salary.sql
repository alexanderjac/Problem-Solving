CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      with cte as (select salary, dense_rank() over (order by salary desc) as rk from employee)
      select distinct salary as getNthHighestSalary from cte where   rk = N
      
  );
END