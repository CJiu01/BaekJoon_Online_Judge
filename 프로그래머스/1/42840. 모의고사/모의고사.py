def solution(answers):
    student1 = [1,2,3,4,5]
    student2 = [2,1,2,3,2,4,2,5]
    student3 = [3,3,1,1,2,2,4,4,5,5]
    
    s1, s2, s3 = 0,0,0
    for i in range(len(answers)):
        if answers[i] == student1[i%5]:
            s1 += 1
        if answers[i] == student2[i%8]:
            s2 += 1
        if answers[i] == student3[i%10]:
            s3 += 1
    
    answers = []
    max_value = max(s1,s2,s3)
    if s1 == max_value:
        answers.append(1)
    if s2 == max_value:
        answers.append(2)
    if s3 == max_value:
        answers.append(3)
        
    return answers