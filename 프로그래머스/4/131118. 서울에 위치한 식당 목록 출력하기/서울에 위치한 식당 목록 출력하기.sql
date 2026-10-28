select RI.REST_ID, REST_NAME, FOOD_TYPE, FAVORITES, ADDRESS, SCORE
from REST_INFO as RI join (
    select REST_ID, round(avg(REVIEW_SCORE),2) as SCORE
    from REST_REVIEW
    group by REST_ID
) as RR
on RI.REST_ID = RR.REST_ID
where ADDRESS like '서울%'
order by SCORE desc, FAVORITES desc
