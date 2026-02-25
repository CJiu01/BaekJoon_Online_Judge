-- 코드를 입력하세요
# select USER_ID, PRODUCT_ID
# from ONLINE_SALE
# group by user_id, product_id
# having count(*)>1
# order by USER_ID, PRODUCT_ID DESC

select USER_ID, PRODUCT_ID
from ONLINE_SALE
group by USER_ID, PRODUCT_ID
having count(*)>1
order by USER_ID, PRODUCT_ID DESC