# Write your MySQL query statement below

select b.category, count(account_id) as accounts_count
from
(select account_id,income,
case when income<20000 then 'Low Salary'
 when income between 20000 and 50000 then 'Average Salary'
 when income >50000 then 'High Salary' end as category

from Accounts) a

right join

(select 'Low Salary' as category
union 
select 'Average Salary' as category
union
select 'High Salary' as category) b

on a.category=b.category
group by b.category