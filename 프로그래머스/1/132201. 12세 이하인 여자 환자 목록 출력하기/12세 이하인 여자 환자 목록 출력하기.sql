-- 코드를 입력하세요
select PT_NAME, PT_NO, GEND_CD, AGE, IFNULL(TLNO, 'NONE') AS TLNO
from patient
where gend_cd = 'w' and age<=12
order by age desc, pt_name