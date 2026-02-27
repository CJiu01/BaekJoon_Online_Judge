-- 코드를 입력하세요
select INGREDIENT_TYPE, sum(TOTAL_ORDER) as TOTAL_ORDER
from FIRST_HALF F join ICECREAM_INFO I on (F.Flavor = I.Flavor)
group by INGREDIENT_TYPE
order by TOTAL_ORDER