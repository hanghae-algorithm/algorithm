import sys

# 1. 점 개수 입력 
# 2. 빈 리스트 만들기
# 3. 입력 개수만큼 x, y> y, x 형태로 리스트에 추가
# 4. y, x에 대해 오름차순 정렬 참고로 내림차순은 s = sorted(array, reverse=True)
# 5. y, x에 대해 정렬된 배열을 x, y로 위치 바꾸고 프린트하기
n = int(sys.stdin.readline()) #첫번째 인풋 점의 개수
array = []                    #빈 배열 만들기

for i in range(n):            #점의 개수 만큼 반복한다.
    x, y = map(int, sys.stdin.readline().split())   # 각 점의(x, y좌표)
    array.append([y, x])                  #빈 배열에 y, x를 넣어준다(순서바뀜)

s = sorted(array)             #배열의 순서를 정렬해준다. (y에 대해 오름차순 이후 x에 대해 오름차순)

for a, b in s:                #y,x 형식으로 정렬된 배열을 x, y 형식으로 한줄씩 출력한다.
    print(b, a) 
    
# for R in range(len(s)):
#      print(s[R][1], s[R][0])

# for 문 표현만 다르게 한 경우
# n = int(input())
# array = []

# for i in range(n):
#     x, y = map(int, input().split())
#     array.append([y, x])

# s = sorted(array)  

# for _ in range(len(s)):
#      print(s[_][1], s[_][0])

# https://guku.tistory.com/28         11651 본인 문제 풀이 과정
# https://oort-cloud.tistory.com/28   11651 문제 풀이 예시
# https://dojang.io/mod/page/view.php?id=2292  2차원 리스트 모두 출력하기