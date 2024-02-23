-- 코드를 입력하세요
SELECT WAREHOUSE_ID,WAREHOUSE_NAME, ADDRESS, Ifnull(FREEZER_YN, 'N')
from FOOD_WAREHOUSE
where address like '경기도%'
order by WAREHOUSE_ID