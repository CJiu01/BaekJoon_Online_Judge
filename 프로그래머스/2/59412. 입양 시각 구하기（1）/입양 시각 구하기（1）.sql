-- 코드를 입력하세요
SELECT hour(datetime), count(*) as count
from ANIMAL_OUTS
where time(datetime) between '09:00' and '19:59'
group by hour(datetime)
order by hour(datetime)