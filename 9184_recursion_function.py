# # 작성일 : 21-06-22
# # 주제 : 동적 계획법
# # 난이도 : 중
# # 담당자 : 윤송
#
# # 백준 코드번호 : 9184
# url: https://www.acmicpc.net/problem/2108
# # 문제명 : 신나는 함수 실행
# # 문제설명 :
# 보기와 같이 주어진 재귀함수를 출력하는 프로그램 작성

## 풀이 방법
# 1. 함수 결과를 저장할 수 있는 'memo' 배열을 생성한다
# 2. 수식이 끝난 후 'memo'에 값을 저장한다.
# 3. 만약 이미에 'memo'에 값이 있다면 수식을 진행하지 않고 값만 바로 빼간다.
# 4. 2,3번을 input값으로 -1,-1,-1이 나올 때까지 반복한다.

import sys
# 메모이제이션 배열
memo = {}


def w(a, b, c, w_memo):

    # 메모에 저장해놓은 값이 있다면 찾아온다.
    if (a, b, c) in w_memo:
        return w_memo[a, b, c]

    if a <= 0 or b <= 0 or c <= 0:
        result = 1
    elif a > 20 or b > 20 or c > 20:
        result = w(20, 20, 20, w_memo)
    elif a < b < c:
        result = w(a, b, c-1, w_memo) + w(a, b-1, c-1, w_memo) - w(a, b-1, c, w_memo)
    else:
        result = w(a-1, b, c, w_memo) + w(a-1, b-1, c, w_memo) + w(a-1, b, c-1, w_memo) - w(a-1, b-1, c-1, w_memo)

    # 메모에 값 저장
    w_memo[(a, b, c)] = result
    # print(w_memo)

    return result


while True:
    num1, num2, num3 = map(int, sys.stdin.readline().split())
    ans = w(num1, num2, num3, memo)
    if all([num1 == -1, num2 == -1, num3 == -1]):
        break
    print(f'w({num1}, {num2}, {num3}) = {ans}')
