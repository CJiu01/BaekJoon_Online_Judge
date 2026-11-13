select A.ID, count(B.PARENT_ID) CHILD_COUNT
from ECOLI_DATA A left outer join ECOLI_DATA B on (A.ID = B.PARENT_ID)
group by A.ID