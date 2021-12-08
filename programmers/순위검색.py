from bisect import bisect_left
from itertools import combinations

def make_all_cases(separate_info):
    cases = []
    for k in range(5):
        for condition in combinations([0,1,2,3], k):
            case = []
            for idx in range(4):
                if idx not in condition:
                    case.append(separate_info[idx])
                else:
                    case.append('-')
            cases.append(''.join(case))
    return cases

def solution(info, query):
    answer = []
    all_people = {}
    for i in info:
        seperate_info = i.split()
        cases = make_all_cases(seperate_info)
        for case in cases:
            if case not in all_people.keys():
                all_people[case] = [int(seperate_info[4])]
            else:
                all_people[case].append(int(seperate_info[4]))
    
    for key in all_people.keys():
        all_people[key].sort()
        
    for q in query:
        q = q.split(' and ')
        q.extend(q.pop().split())
        target = ''
        target = "".join([s for s in q[:4]])
        if target in all_people.keys():
            idx = bisect_left(all_people[target], int(q[4]), lo=0, hi=len(all_people[target]))
            cnt = len(all_people[target]) - idx
            answer.append(cnt)
        else:
            answer.append(0)
    return answer