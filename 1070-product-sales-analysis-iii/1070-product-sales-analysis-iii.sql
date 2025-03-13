# Write your MySQL query statement below

select product_id,first_year,quantity,price
from 
(select product_id, quantity, price, year as first_year,
rank() over (partition by product_id order by year) as rnk

from Sales
) a
where rnk=1

