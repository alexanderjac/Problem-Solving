CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    SET N = N-1;
  RETURN (
      # Write your MySQL query statement below.
      # with cte as (select salary, dense_rank() over (order by salary desc) as rk from employee)
      # select distinct salary as getNthHighestSalary from cte where   rk = N
      # DECLARE @M INT
      # SET @M = N-1
      select distinct salary as getNthHighestSalary from employee 
      order by salary desc
      limit 1
      offset N
      
  );
END
