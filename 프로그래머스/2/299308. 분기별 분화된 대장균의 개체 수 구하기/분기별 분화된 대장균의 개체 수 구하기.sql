-- 코드를 작성해주세요
select CONCAT(QUARTER(DIFFERENTIATION_DATE),"Q") Q, count(*) ECOLI_COUNT
from ECOLI_DATA
group by Q
order by Q