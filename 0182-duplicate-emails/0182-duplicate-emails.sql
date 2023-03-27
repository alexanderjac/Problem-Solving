/* Write your T-SQL query statement below */
select email from Person
group by email
having count(Email)>1