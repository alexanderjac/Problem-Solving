/* Write your T-SQL query statement below */
select 
    d.name as Department, e.name as Employee, salary
from
        Department d join Employee e
        on d.id = e.departmentId
where (e.departmentId, Salary) in (
    select 
            DepartmentID, max(Salary)
    From
            Employee
    Group By 
            DepartmentID
    
)
