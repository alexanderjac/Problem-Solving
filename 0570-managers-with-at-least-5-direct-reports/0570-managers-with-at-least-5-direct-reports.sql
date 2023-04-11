# Write your MySQL query statement below
with cte as (
select 
       m.name, count(e.id) as reports
from 
     Employee m join Employee e
on   m.id = e.managerId
group by 1
)

select name from cte where reports>=5

     