-- 코드를 입력하세요
set @hour = -1;
select (@hour := @hour + 1) as hour,
        (
            select count(hour(datetime))
            from ANIMAL_OUTS
            where @hour = hour(datetime)
        ) as count
from ANIMAL_OUTS
where @hour < 23