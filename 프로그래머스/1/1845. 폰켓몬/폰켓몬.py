def solution(nums):
    
    poncatmon_kind_num = len(set(nums))
    catch_num = len(nums) // 2
    result = min(poncatmon_kind_num, catch_num)

    return result