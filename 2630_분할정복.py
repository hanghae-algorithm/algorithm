#분할정복(Divide and conquer) 이란?
#어떤 문제를 해결하는 알고리즘에서 원래 문제를 성질이 똑같은 여러개의
#부분 문제로 나누어 해결하여 원래 문제의 해를 구하는 방식.

#분할 정복은 다음과 같은 절차를 거친다.
#1.Divide
#2개 이상의 작은 문제들로 쪼갠다.
#2. Conquer
#나누어진 작은 문제들을 푼다.
#3.Combine
#나누어 해결한 문제들을 합친다.

#global문이란? 전역변수를 수정할수 있는 구문.
#전역변수: 함수 밖, 전역 이름공간에 정의된 변수.
#지역변수: 함수 안, 지역 이름공간에 정의된 변수.
#지역변수는 그 변수가 정의된 함수 안에서만 읽을 수 있다.
#전역변수는 프로그램 어디서든 읽을 수 있다. 단, 함수 안에서 전역변수에 새로운 값을 대입할 수는 없다.
#함수 내에서는 x행,y열,종이의 크기 n이 정의가 되어있는 지역 변수이다.
#따라서 우리가 구하려는 하얀색,파란색 종이의 갯수를 구하기 위해서는 x,y,n이 정의된 함수내에서 하얀,파란종이 갯수를 카운트를
#해야 하기 때문에 전역변수를 수정할수 있는 global구문에 삽입해 수정할 수 있다.

#풀이과정
# 1. 전체 범위부터 값이 한 가지 값으로만 이루어져 있는지 확인(check함수)

#2. 4등분하여 각 등분한 부분마다 한 가지 값으로 이루어져 있는지 확인(재귀)

#3. 확인이 된 부분은 어떤값으로(0 or 1) 이루어져 있는지 확인하고 값에 따라 white, blue 값 카운트 업(solve함수)

#4. 확인이 안된 부분은 또 한 번 4등분

#참고 블로그 : https://data-jj.tistory.com/38

import sys
input = sys.stdin.readline
n = int(input())

paper = []
for i in range(n):
    paper.append(list(map(int,input().split())))

white = 0 #값이 0이면 흰색 카운트 업
blue = 0  #값이 1이면 파란색 카운트 업


def check(x,y,n):                #값이 하나로 일치하는지 체크하는 역할
    compare_color = paper[x][y]  #비교할 기준 색깔을 정한다.
    for i in range(0,x+n):
        for j in range(0,y+n):
            if paper[i][j] != compare_color:
                return False
    return True

def solve(x,y,n):              #check해서 아니면 쪼개면서 white,blue가 몇개인지 검증하는 역할
    global white,blue

    if check(x,y,n):
        if paper[x][y] == 0:
            white += 1
        else:
            blue += 1
        return
    else:
        n //= 2
        solve(x,y,n)
        solve(x,y+n,n)
        solve(x+n,y,n)
        solve(x+n,y+n,n)
        return

solve(0,0,n)
print(white)
print(blue)



# import sys
# input = sys.stdin.readline
# n = int(input())
# color_paper = []
# for i in range(n):
#     color_paper.append(list(map(int,input().split()))) # x행,y열
# white = 0 #0이면 흰색     white,blue 둘다 전역변수
# blue = 0 #1이면 파란색
#
# def cut(x,y,n):
#     global blue,white
#     check = color_paper[x][y]
#     for i in range(x,x+n):
#         for j in range(y,y+n):
#             if check != color_paper[i][j]: #하나라도 같은색이 아니라면
#                 cut(x,y,n//2) #1사분면
#                 cut(x+n//2,y,n//2)  # 2사분면
#                 cut(x,y+n//2,n//2) #3사분면
#                 cut(x+n//2,y+n//2,n//2) #4사분면
#
#
#     if check == 0: #모두 흰색일때
#         white +=1
#         return
#     else: #모두 파란색일떄
#         blue += 1
#         return
#
# cut(0,0,n)
# print(white)
# print(blue)