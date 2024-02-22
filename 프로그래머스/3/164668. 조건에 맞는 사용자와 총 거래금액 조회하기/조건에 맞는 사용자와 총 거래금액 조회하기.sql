-- 코드를 입력하세요
SELECT B.user_id, B.nickname, sum(price) as TOTAL_SALES
from USED_GOODS_BOARD A 
inner join USED_GOODS_USER B on A.writer_id = B.user_id
where A.STATUS='DONE' 
group by B.user_id
having TOTAL_SALES >= 700000
order by TOTAL_SALES
