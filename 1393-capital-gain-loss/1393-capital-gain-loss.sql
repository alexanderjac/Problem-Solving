/* Write your T-SQL query statement below */

select stock_name, sum(case when operation = 'Buy' then -1*price 
else price end ) as capital_gain_loss
from Stocks
group by stock_name
