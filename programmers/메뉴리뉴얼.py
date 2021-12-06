from itertools import combinations

def solution(orders, course):
    answer = []
    orders = [''.join(sorted(order)) for order in orders]

    course_menu = dict()
    for c in course:
        for order in orders:
            # 메뉴 코스 개수보다 단품 개수가 적으면 넘어간다.
            if len(order) < c:
                continue
            # 해당 코스의 내용 개수만큼의 메뉴로 조합을 만든다.
            # 각 코스메뉴별로 몇 명의 손님이었는지 숫자를 확인한다.
            for combi in combinations(order, c):
                menu = ''.join(combi)
                if menu in course_menu:
                    course_menu[menu] += 1
                else:
                    course_menu[menu] = 1
                    
    # 횟수가 2회보다 적거나, 더 큰 코스메뉴의 횟수보다 작다면 제외
    for k, v in course_menu.items():
        if v < 2:
            continue
        for k2, v2 in course_menu.items():
            # 같은 코스 메뉴는 비교 대상에서 제외
            if k == k2:
                continue
            # 코스의 길이가 같을 경우 횟수가 적다면 제외
            if len(k) == len(k2) and v < v2:
                break
            # 같은 메뉴를 포함한 더 큰 코스메뉴의 횟수보다 적다면 제외
            if len(k) < len(k2) and set(k).issubset(set(k2)) and v < v2:
                break
        else:
            answer.append(k)

    return sorted(answer)