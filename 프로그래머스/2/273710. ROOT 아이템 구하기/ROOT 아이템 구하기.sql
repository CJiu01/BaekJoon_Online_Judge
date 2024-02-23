-- 코드를 작성해주세요
select II.ITEM_ID, II.ITEM_NAME
from ITEM_TREE IT
inner join ITEM_INFO II on (IT.item_id = II.item_id)
where IT.PARENT_ITEM_ID is null
order by II.item_id