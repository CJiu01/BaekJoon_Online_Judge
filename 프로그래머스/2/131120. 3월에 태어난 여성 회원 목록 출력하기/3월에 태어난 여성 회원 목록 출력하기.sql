select MEMBER_ID, MEMBER_NAME, GENDER, DATE_OF_BIRTH
from MEMBER_PROFILE
where TLNO is not null and month(DATE_OF_BIRTH) = '03' and GENDER = 'W'
order by MEMBER_ID