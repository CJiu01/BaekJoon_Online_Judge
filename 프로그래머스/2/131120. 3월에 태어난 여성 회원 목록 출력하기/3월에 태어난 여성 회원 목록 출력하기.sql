select MEMBER_ID, MEMBER_NAME, GENDER, date_format(DATE_OF_BIRTH, '%Y-%m-%d') DATE_OF_BIRTH
from MEMBER_PROFILE
where tlno is not null and month(date_of_birth) like '3' and gender = 'W'
order by member_id
