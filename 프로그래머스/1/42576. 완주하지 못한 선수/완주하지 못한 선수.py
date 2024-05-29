from collections import Counter

def solution(participant, completion):
    participant = Counter(participant)
    completion = Counter(completion)
    participant.subtract(completion)
    
    return ''.join(list(participant.elements()))
