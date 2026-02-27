-- 코드를 입력하세요
select truncate(price, -4) PRICE_GROUP, count(*) PRODUCTS
from product
group by PRICE_GROUP
order by PRICE_GROUP














# SELECT truncate(price, -4) as PRICE_GROUP, count(*) as PRODUCTS
# from product
# group by PRICE_GROUP
# order by PRICE_GROUP