import sys

input = sys.stdin.readline

a, b = map(int, input().split())


# a!/b!(a-b)!

def factorial(n):
    if n > 0:
        return n * factorial(n - 1)
    else:
        return 1


print(factorial(a) // (factorial(b) * factorial(a - b)))

# 고등학교때 배웠던 콤비네이션 문제이다!!
# 팩토리얼은 재귀함수!!!!!
