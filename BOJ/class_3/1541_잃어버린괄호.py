import re

expr = input()
expr = re.split('([\-\+])',expr)

while '+' in expr:
    for i, s in enumerate(expr):
        if s == '+':
            expr[i-1] = int(expr[i-1]) + int(expr[i+1])
            expr = expr[:i] + expr[i+2:]
            break

answer = int(expr[0])
for s in expr[1:]:
    if s != '-':
        answer -= int(s)

print(answer)