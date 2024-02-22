-- 코드를 입력하세요
SELECT year(os.sales_date) as year, 
        month(os.sales_date) as month, 
        UI.gender, 
        count(distinct UI.user_id) as 'USERS'
from ONLINE_SALE as OS
inner join USER_INFO as UI on (OS.user_Id = UI.user_Id)

where UI.GENDER is not null
group by year(os.sales_date), month(os.sales_date), UI.gender
order by year, month, gender