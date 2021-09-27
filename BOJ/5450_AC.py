import sys
from collections import deque

def process(p,array):
    direction = True
    for func in p:
        if func == 'R':
            direction = not direction
        else:
            if len(array) < 1:
                return 'error'
            if direction:
                array.popleft()
            else:
                array.pop()

    if not direction:
        array.reverse()

    return str(list(array)).replace(' ', '')


for _ in range(int(input().rstrip())):
    p = input().rstrip()
    n = int(input().rstrip())
    array = input().rstrip()[1:-1]

    if array == '':
        array = deque([])
    else:
        array = deque(map(int, array.split(',')))
    print(process(p, array))