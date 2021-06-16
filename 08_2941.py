a = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
b = input()

# 1

for i in a:
    b = b.replace(i, '*')

print(len(b))

# 2
from collections import Counter

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for c in croatia:
    word = word.replace(c, '1')

print(sum(Counter(word).values()))  # counter.values() : 각 요소의 빈도수. word의 각 요소의 빈도수를 더한다.

# 3

s = input()

l = len(s)
result = l

for i in range(1, l):
    if s[i] == 'j':  # s의 i 번째 값이 'j'라면
        if s[i - 1] == 'l' or s[i - 1] == 'n':  # 그 앞글자가 (i-1) l이거나 n이라면
            result -= 1  # 카운트 -1 (무조건 1개의 알파벳으로 이루어져 쓰이기 때문)
    elif s[i] == '-':  # '-'라면
        if s[i - 1] == 'c' or s[i - 1] == 'd':  # (d-,c-)의 경우도 1글자라고 생각함
            result -= 1
    elif s[i] == '=':  # '='라면
        if s[i - 1] == 'c' or s[i - 1] == 's':  # (c=, s=)의 경우 1글자라고 생각함.
            result -= 1
        elif s[i - 1] == 'z':  # 'z' 라면(dz=, z=)
            if s[i - 2] == 'd':  # (dz=)
                result -= 2  # 3글자니까 -2글자 해야함
            else:
                result -= 1  # (z=)

print(result)
