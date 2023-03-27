# Write your MySQL query statement below

with result as (
select 
        d.name as Department , e.name as Employee, e.salary, dense_rank() over (partition by departmentID order by salary desc) as salaryRank
From
      Department d join Employee e
      on d.id = e.departmentId
)

select 
        Department, Employee, salary
From 
        result
where   
        salaryRank<=3


# select 
#     d.name as Department, E.name as Employee, E.Salary       
# From 
#      Department d join Employee E
#      on d.id = E.departmentID
# where (departmentID, salary) in (

# select 
#      departmentId, (select Salary 
#                     from Employee E
#                     where E.departmentId = d.departmentId
#                     order by Salary desc
#                     Limit 3)
#     from Employee d
# )