# Write your MySQL query statement below

# with cte as (
# select num, count(*) as count from logs
#     group by num
# )

# select count(*) from cte where count>=3

select distinct a.num as ConsecutiveNums from logs a join logs b  
on a.id = b.id+1 and a.num = b.num 
join logs c on a.id = c.id+2 and a.num = c.num