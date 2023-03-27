# Write your MySQL query statement below

# with result as (
# select 
#         d.name as Department , e.name as Employee, e.salary, dense_rank() over (partition by departmentID order by salary desc) as salaryRank
# From
#       Department d join Employee e
#       on d.id = e.departmentId
# )

# select 
#         Department, Employee, salary
# From 
#         result
# where   
#         salaryRank<=3


SELECT
    d.Name AS 'Department', e1.Name AS 'Employee', e1.Salary
FROM
    Employee e1
        JOIN
    Department d ON e1.DepartmentId = d.Id
WHERE
    3 > (SELECT
            COUNT(DISTINCT e2.Salary)
        FROM
            Employee e2
        WHERE
            e2.Salary > e1.Salary
                AND e1.DepartmentId = e2.DepartmentId
        )