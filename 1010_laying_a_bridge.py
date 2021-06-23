# 1010, 다리 놓기 DP 방법 https://li-fo.tistory.com/60  / https://guku.tistory.com/32
import sys

t = int(sys.stdin.readline())
dp = [[0]*30 for _ in range(30)]     # dp 테이블 만들기


for i in range(30):            # 0~ 29까지 반복   (N과 M의 범위)
    for j in range(30):        # i 0 j0~29, i 1 j 0~29
        if i == 1:
            dp[i][j] = j
        else:
            if i == j:
                dp[i][j] = 1
            elif i < j:
                dp[i][j] = dp[i-1][j-1] + dp[i][j-1]

for i in range(t):
    n, m = map(int, sys.stdin.readline().split())
    print(dp[n][m])

# # 조합이용 factorial 정의 nCr = n! / r! *(n - r)!    https://roamingman.tistory.com/5
# def facto(x):
#     if x == 0 or x == 1:
#         return 1
#     else:
#         return x * facto(x-1)
 
# def comb(n, r):
#     return int(facto(n) / (facto(r) * facto(n-r)))
 
# def solve():
#     a, b = [int(x) for x in input().split()]
#     print(comb(b, a))
 
# t = int(input())
# for _ in range(t):
#     solve()

# math 모듈 이용 쉬운 풀이
# import math

# T = int(input())

# for _ in range(T):
#     n, m = map(int, input().split())
#     mCn = math.factorial(m) // (math.factorial(n) * math.factorial(m - n))
#     print(mCn)



# # # 1010, 다리 놓기 조합이용 nCr = n! / r! *(n - r)!  
# # import sys
# # t = int(sys.stdin.readline())

# # for i in range(t):
# #     n, m = map(int, sys.stdin.readline().split())
# #     if n == m:
# #         print(1)
# #     else:
# #         ans = 1
# #         for i in range(m, m-n, -1):
# #             ans *= i
# #         for j in range(n, 1, -1):
# #             ans = ans // j
# #         print(ans)


# # # 이해 못했는데 쉬워보임
# # T = int(input())

# # for _ in range(T):
# #     m, n = map(int, input().split())
# #     answer = 1
# #     k = n - m
    
# #     while n > k:
# #         answer *= n
# #         n -= 1
# #     while m > 1:
# #         answer = answer // m
# #         m -= 1
    
# #     print(answer)