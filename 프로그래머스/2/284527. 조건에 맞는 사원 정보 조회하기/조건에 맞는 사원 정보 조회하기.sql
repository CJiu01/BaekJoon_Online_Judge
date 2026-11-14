select SCORE,C.EMP_NO,EMP_NAME,POSITION,EMAIL
from HR_DEPARTMENT A join HR_EMPLOYEES B on (A.DEPT_ID = B.DEPT_ID)
join (
    select EMP_NO, sum(SCORE) SCORE
    from HR_GRADE
    group by EMP_NO
) C on (B.EMP_NO = C.EMP_NO)
order by SCORE desc
limit 1