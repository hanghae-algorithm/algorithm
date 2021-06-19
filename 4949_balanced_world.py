# # 작성일 : 21-06-19
# # 주제 : 스택
# # 난이도 : 중
# # 담당자 : 윤송

# # 백준 코드번호 : 4949
# # 문제명 : 균형잡힌 세상
# # 문제설명 :'()' 와 '[]' 짝이 있을 경우 'yes'를 반환 아닐 경우 'no'를 반환한다.
#             '.'과 같이 괄호가 하나도 없는 경우에도 'yes'를 반환한다.


# # 풀면서 어려웠던 점
# 백준에서 주는 예제외에 추가 조건들이 있었는데, 그걸 찾는게 어려웠음

# # 배운 것들
# deque vs list
# deque: double ended queue의 줄임말로 컨테이너의 양방향 (시작과 끝) 위치에 접근이 가능한 자료형이다. (leftpop(), pop())
#        원소들에 index로 직접 접근이 가능하며 앞, 끝에 삽입/제거가 빠르다. (stack, queue에 적합)
#        단, 시작, 끝 위치가 아닌 위치에서 삽입,제거 수행 시 list에 비해 성능이 떨어진다.
# list: 컨테이너내 어느 위치에서도 삽입, 제거가 빠르다.
#       어느 위치에 있든 원소들의 순서 이동이 빠르다.
#       단, index로 접근이 불가능하며 특정 원소에 접근 시 선형탐색을 이용해야하므로 비효율적이다.
# 참고 : http://egloos.zum.com/sweeper/v/2817817

# input() vs sys.stdin.readline()
# input(): 입력값을 받으면 문자열을 변환 후 strip()를 진행하는 과정을 거친다.
#          또한 input()을 사용하면 입력값을 받을 수 있는 prompt(일종의 입력창)를 가지고 있는데, 대량의 값을 받을 시 입력을 받고 prompt를 띄우는 과정을 반복하므로
#          성능이 떨어질 수 밖에 없다.
#          파이썬의 내장함수로 취급되며 입력된 값이 없을 시 오류가 발생한다.
# sys.stdin.readline(): input()과 동일하게 입력값을 받지만 strip() 과정이 없기에 개행문자(엔터 형태)를 받을 수 있다.
#                       또한, 입력값에 제한을 줘 문자의 수를 정할 수도 있다. (ex. sys.stdin.readline(2) 일 시, 입력된 문자열 중 첫 두개의 문자만 출력)
#                       *sys 라이브러리에 속하는 file object로 취급되기에 prompt가 아닌 사용자의 입력만을 받는 **buffer를 만들어 읽어들인다.
#                       입력된 값이 없을 시 빈 문자열로 반환한다.
#       *sys란, c언어로 작성되어 있는 파이썬이 제공하는 모듈이다. (파이썬 인터프리터가 제공하는 변수와 함수를 직접 제어할 수 있게 해준다.)...공부 필요필요..
#      **buffer란, 임시 저장 공간으로서 input,output를 수행할 때 속도차이를 극복하기 위해 사용된다. (prompt보다 효율적이라고 생각하면 될 듯..)
# 참고: https://velog.io/@gouz7514/%ED%8C%8C%EC%9D%B4%EC%8D%AC-input-vs-sys.stdin.readline


# # 해결 방법
# 1. deque를 이용하여 stack를 생성한다.
# 2. '(','[' 같이 열린 괄호는 stack에 넣어준다.
# 3. 입력된 문자열의 문자들을 하나씩 돌며 ')'나 ']'같이 닫힌 괄호들이 있으면 앞서 2에서 넣은 값을 stack.pop()을 이용해서 제거한다.
# 4. 문자열의 문자 수만큼 2와 3을 반복한 후 stack에 값이 없다면 모든 괄호들이 짝이 맞다는 뜻이므로 yes, 아니라면 no를 출력한다.
# 참고 1. 문자열이 소괄호라면 스택의 마지막값도 소괄호여야하고 대괄호라면 똑같이 대괄호여야한다. (만약 다를 시 균형잡힌 문자열이 아니므로 no 출력)
# 참고 2. 스택의 값이 모두 사라졌음에도 문자열 아직도 열린 괄호가 남아있다면 괄호들의 짝이 맞지 않는다는 뜻이므로 no 출력

import sys
from collections import deque

while True:
    result = ''
    string = sys.stdin.readline().rstrip()
    if string == '.':
        break
    
    # 스택 생성
    stack = deque()
    for char in string:
        # 문자가 열린 괄호일 시 스택에 추가
        if char == '(' or char == '[':
            stack.append(char)
        # Case1. 문자가 닫힌 소괄호이며 stack에 제일 최근에 넣은 값도 소괄호라면 stack.pop()
        elif char == ')':
            if stack and stack[-1] == '(':
                stack.pop()
        # Case2. 문자가 닫힌 소괄호지만 stack에 값이 없거나 최근에 넣은 값이 소괄호가 아니라면 짝이 안맞으므로 result 변수에 'no' 저장
            elif not stack or stack[-1] == '[':
                result = 'no'
                break
        # Case3. 문자가 닫힌 대괄호이며 stack에 제일 최근에 넣은 값도 대괄호라면 stack.pop()
        elif char == ']':
            if stack and stack[-1] == '[':
                stack.pop()
        # Case4. 문자가 닫힌 대괄호지만 stack에 값이 없거나 최근에 넣은 값이 대괄호가 아니라면 짝이 안맞으므로 result 변수에 'no' 저장
            elif not stack or stack[-1] == '(':
                result = 'no'
                break

    # 만약 stack에 값이 없거나 result에 할당된 값이 없다면 균형 문자열이므로 yes 저장
    if len(stack) == 0 and result == '':
        result = 'yes'
    # else, no 저장
    else:
        result = 'no'

    # 결과 출력
    print(result)
