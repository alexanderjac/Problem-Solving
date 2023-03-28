# Write your MySQL query statement below

with result as(
SELECT
        request_at,
        sum(case when status != 'completed' then 1 
        else 0 end ) as cancelled_no, count(distinct id) as total
FROM
        Trips t JOIN Users u
        ON t.client_id = u.users_id
where 
        request_at between '2013-10-01' and '2013-10-03'
        AND t.client_id not in (select users_id from Users where banned ='Yes')
        AND t.driver_id not in (select users_id from Users where banned ='Yes')
Group by
        request_at)
        
select request_at as Day,   round(cancelled_no/(total),2) as 'Cancellation Rate' from result
        
        
        # Write your MySQL query statement below
# SELECT
#     request_at AS Day,
#     ROUND((SUM(CASE WHEN status != 'completed' THEN 1 ELSE 0 END)/COUNT(DISTINCT id)),2) AS 'Cancellation Rate'
# FROM Trips
# WHERE request_at BETWEEN '2013-10-01'
# AND '2013-10-03'
# AND client_id NOT IN (
#     SELECT
#         users_id
#     FROM Users
#     WHERE banned = 'Yes'
# )
# AND driver_id NOT IN (
#     SELECT
#         users_id
#     FROM Users
#     WHERE banned = 'Yes'
# )
# GROUP BY request_at;