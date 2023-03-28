# Write your MySQL query statement below

with result as (
    select id, recordDate, temperature ,lag(recordDate) over(order by recordDate) as prevrecordDate, lag(temperature) over(order by recordDate) as prevtemperature from weather
)

select id from result 
where temperature>prevtemperature and datediff(prevrecordDate,recordDate  ) =-1