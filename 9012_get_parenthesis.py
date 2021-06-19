# # 작성일 : 21-06-19
# # 주제 : 스택
# # 난이도 : 중
# # 담당자 : 윤송
#
# # 백준 코드번호 : 4949
# # 문제명 : 균형잡힌 세상
# # 문제설명 :'()' 와 '[]' 짝이 있을 경우 'yes'를 반환 아닐 경우 'no'를 반환한다.
#             '.'과 같이 괄호가 하나도 없는 경우에도 'yes'를 반환한다.


# # 해결 방법
import sys
from collections import deque

while True:
    string = sys.stdin.readline().rstrip()
    if string == '.':
        break;

    stack = deque()
    for i in range(len(string)):
        if string[i] == '(' or string[i] == '[':
            stack.append(string[i])
        elif stack:
            if string[i] == ')' and stack[-1] == '(':
                stack.pop()
            elif string[i] == ']' and stack[-1] == '[':
                stack.pop()

    if len(stack) == 0:
        print('yes')
    else:
        print('no')





