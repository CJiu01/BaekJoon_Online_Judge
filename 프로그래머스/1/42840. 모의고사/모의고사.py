def solution(answers):
    student_1 = [1, 2, 3, 4, 5]
    student_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    collects = [0,0,0]
    result = []
    
    for i, answer in enumerate(answers):
        if student_1[i % len(student_1)] == answer:
            collects[0] += 1
        if student_2[i % len(student_2)] == answer:
            collects[1] += 1
        if student_3[i % len(student_3)] == answer:
            collects[2] += 1

    for i, collect in enumerate(collects):
        if max(collects) == collect:
            result.append(i+1)
    return result