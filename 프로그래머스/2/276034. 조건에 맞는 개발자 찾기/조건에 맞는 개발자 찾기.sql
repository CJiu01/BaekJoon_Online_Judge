-- 코드를 작성해주세요
select ID, EMAIL, FIRST_NAME, LAST_NAME
from DEVELOPERS
where SKILL_CODE & (select code from SKILLCODES where NAME='Python')
    OR SKILL_CODE & (select code from SKILLCODES where NAME='C#')
order by ID