-- 코드를 입력하세요
SELECT I.NAME, I.DATETIME
FROM ANIMAL_INS I left join ANIMAL_OUTS O USING(ANIMAL_ID)
WHERE O.DATETIME IS NuLL
ORDER BY I.DATETIME
LIMIT 3