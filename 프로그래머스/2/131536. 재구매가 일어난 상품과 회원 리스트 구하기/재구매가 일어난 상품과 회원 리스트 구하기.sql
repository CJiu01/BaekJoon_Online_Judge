-- 코드를 입력하세요
# select USER_ID, PRODUCT_ID
# from ONLINE_SALE
# group by user_id, product_id
# having count(*)>1
# order by USER_ID, PRODUCT_ID DESC

select user_id,product_id
from ONLINE_SALE

group by user_id,product_id
having count(*) >1
order by user_id,product_id desc










