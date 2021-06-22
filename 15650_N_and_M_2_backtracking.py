# # 작성일 : 21-06-21
# # 주제 : 백트랙킹
# # 난이도 : 중
# # 담당자 : 윤송
#
# # 백준 코드번호 : 15650
# url: https://www.acmicpc.net/problem/15650
# # 문제명 : N과 M(2)
# # 문제설명 :
# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
# * 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
# * 고른 수열은 오름차순이어야 한다

# # 풀이전 생각할 것
# 재귀함수를 이용한 DFS를 구현하되 조건에 맞지않으면 종료될 수 있도록 하자
# input값으로 받은 수열을 인전 리스트를 이용해서 즉각 연결 여부를 확인할 수 있도록 그래프화 하자.

# # 해결 방법

import sys
# n : 숫자 범위 |  m : 수열 길이
n, m = map(int, sys.stdin.readline().split())
# 중복 접근을 방지하기위해 방문한 값을 기록해놓는 배열
# (0: 방문 X | 1:방문 O)
# n의 범위 만큼 0으로 배열을 채워준다.
visited = [0 for _ in range(n)]
# m의 길이 만큼 수열을 저장할 수 있는 스택
stack = []


def dfs(size):
    # 현재 수열을 담고있는 배열의 길이가 입력값으로 요구한 출력길이와 동일하다면 함수 종료 후 결과값 출력
    if size == m:  # 현재 m == 2
        #  배열에 '*' 추가시 대괄호없이 출력
        print(*stack)
        return
    # size = 0
    # stack = []
    # i = 0
    # visited = [1, 1, 1, 1]
    for i in range(n):  # n이 4일시 -> 0, 1, 2, 3
        if visited[i] == 0:
            visited[i] = 1  # 중복 접근 방지를 위해 1로 변경
            stack.append(i+1)   # 수열 추가
            dfs(size + 1)   # 다음 깊이 탐색
            i = 0
            stack.pop()     # 탐색한 내용은 제거
            # visited 배열이 모두 1로 바뀌었을 때 초반에(i=0)
            # 끝나지않은 재귀함수가 다시 호출이 되어 visited 배열을 다시 0값으로 변경한다.
            for j in range(i+1, n):  # range(4,4)
                visited[j] = 0


dfs(0)

# print
# 1, 2
# 1, 3
#
#

