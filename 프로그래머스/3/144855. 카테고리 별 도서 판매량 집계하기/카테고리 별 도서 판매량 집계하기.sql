-- 코드를 입력하세요
SELECT B.category, sum(BS.sales)
from BOOK_SALES BS
inner join BOOK B on (BS.book_id = B.book_id)
where BS.SALES_DATE like '2022-01%'
group by B.category
order by B.category