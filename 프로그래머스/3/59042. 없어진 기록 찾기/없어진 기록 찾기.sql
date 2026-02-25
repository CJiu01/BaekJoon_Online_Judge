-- 코드를 입력하세요
select AO.ANIMAL_ID, AO.NAME
from ANIMAL_OUTS AO left join ANIMAL_INS AI on (AI.ANIMAL_ID = AO.ANIMAL_ID)
where AI.ANIMAL_ID is null