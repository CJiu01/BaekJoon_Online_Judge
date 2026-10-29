def back(l, n, operand):
    global pool
    if len(l) == n:
        pool.append(l[:])
        return
    
    for i in range(0, n):
        if operand[i] in l:
            continue
        l.append(operand[i])
        back(l, n, operand)
        l.pop()
    return 

def solution(expression):
    global pool
    pool = []
    operand_all = ['-', '+', '*']
    operand = []
    operator = []

    tmp = ''
    # 수식에 있는 연산자 정리
    for s in expression:
        if s in operand_all:
            operand.append(s)
            operator.append(int(tmp))
            tmp = ''
        else:
            tmp += s
    operator.append(int(tmp))
    operand_set = set(operand)
    n = len(operand_set)
    
    # n! 종류 리스트 만들기
    back([], n, list(operand_set))
    
    # 해당 연산자 우선순위에 맞게 연산진행
    answer = 0
    for order in pool:
        tmp_opr = operator[:]
        tmp_opd = operand[:]
        for op in order:
            new_operand = []
            for i in range(len(tmp_opd)):
                if tmp_opd[i] == op:
                    if op == '+':
                        tmp_opr[i+1] = tmp_opr[i] + tmp_opr[i+1]
                        tmp_opr[i] = None
                    elif op == '-':
                        tmp_opr[i+1] = tmp_opr[i] - tmp_opr[i+1]
                        tmp_opr[i] = None
                    elif op == '*':
                        tmp_opr[i+1] = tmp_opr[i] * tmp_opr[i+1]
                        tmp_opr[i] = None
                else:
                    new_operand.append(tmp_opd[i])
            tmp = []
            for j in range(len(tmp_opr)):
                if tmp_opr[j] != None:
                    tmp.append(tmp_opr[j])
            tmp_opr = tmp[:]
            tmp_opd = new_operand[:]
        answer = max(answer, abs(tmp_opr[0]))
        
    return answer