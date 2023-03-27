# Write your MySQL query statement below

with cte as (
select email, count(email) as countEmail from Person
group by email
)
select email from cte where countEmail>1