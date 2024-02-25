-- 코드를 입력하세요
# SELECT MEMBER_ID, MEMBER_NAME, GENDER, date_format(DATE_OF_BIRTH, '%Y-%m-%d') as DATE_OF_BIRTH
# from MEMBER_PROFILE
# where Month(DATE_OF_BIRTH) = 03 and GENDER = 'W' and DATE_OF_BIRTH = TLNO is not null
# order by MEMBER_ID
select MEMBER_ID, MEMBER_NAME, GENDER, date_format(DATE_OF_BIRTH, '%Y-%m-%d')
from MEMBER_PROFILE
where tlno is not null and month(date_of_birth) like '3' and gender = 'W'
order by member_id










