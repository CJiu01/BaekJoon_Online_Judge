-- 코드를 입력하세요
select CAR_TYPE, count(*) CARS
from CAR_RENTAL_COMPANY_CAR
where OPTIONS like '%통풍시트%' or OPTIONS like '%열선시트%' or OPTIONS like '%가죽시트%'
group by CAR_TYPE
order by CAR_TYPE













# SELECT CAR_TYPE, count(*) as cars
# from CAR_RENTAL_COMPANY_CAR
# where options like '%가죽시트%' or options like '%열선시트%' or options like '%통풍시트%'
# group by CAR_TYPE
# order by CAR_TYPE