# Write your MySQL query statement below

SELECT
    a.Name AS 'Employee'
FROM
    Employee AS a join
    Employee AS b
    on a.ManagerId = b.Id
WHERE
    # a.ManagerId = b.Id
        # AND 
        a.Salary > b.Salary

# select   e.name as Employee
#     from employee e, employee m  
# where e.managerId = m.id and e.salary> m.salary