# def solution(skill, skill_trees):
#     answer = 0
    
#     for s in skill_trees:
#         idx = [100] * len(skill)
        
#         for i in range(len(skill)):
#             try:
#                 idx[i] = s.index(skill[i])
#             except ValueError:
#                 idx[i] = 100

#         idx_sorted = sorted(idx)
#         if idx == idx_sorted:
#             answer += 1
            
#     return answer

def solution(skill, skill_trees):
    answer = 0
    
    for skills in skill_trees:
        skill_list = list(skill)
        
        for s in skills:
            if s in skill:
                if s != skill_list.pop(0):
                    break
        else:
            answer += 1
            
    return answer