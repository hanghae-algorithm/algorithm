# 여기서는 DP중 tabulation 방법을 사용한다.

# 계단 3칸까지는 DP의 값이 명확하다.

# 계단 i칸까지 오를때의 최댓값을 dp[i] 라고 놓고

# 문제의 입력(해당 계단의 숫자)를 arr[k] 라고 놓으면

# dp [1] = arr[1]

# dp [2] = arr[1] + arr[2]

# dp [3] = max(arr[1] + arr[3] ,arr[2] + arr[3])

# 4칸째 부터는 생각을 조금 더 해야된다. (3칸 연속되는 계단을 밟을수 없다는 조건때문에)

# 1. dp[i] = dp[i-2] + arr[i]        -> i칸을 밟기 전의 칸이 i-2이므로 3칸 연속밟을일은 없다.

# 2. dp[i] = dp[i-1] + arr[i]        -> i칸 이전에 i-1 칸을 밟았으므로, 3칸 연속일 가능성이 존재한다.

# 따라서 2번 점화식을 바꿔줘야 한다. 한칸 전의 dp가 아닌, 3칸 전의 dp로 이동시킨뒤에 마지막칸은 셀프로 더해주면 3칸 연속일 가능성을 없앨수 있다. 

# 올바른 2번 점화식 : dp[i] = dp[i-3] + arr[i-1] + arr[i]


n = int(input())
dp = [0]*300  [10], [30], [35], 
score = [0]*300  

for i in range(n): 
    score[i] = int(input())

dp[0] = score[0]  
dp[1] = score[0]+score[1]


for j in range(3, n):
    dp[j] = max(score[j]+ dp[j-2], score[j] + score[j-1] + dp[j-3])

print(dp[n-1])
# 코드 참고 : #https://velog.io/@bye9/%EB%B0%B1%EC%A4%80%ED%8C%8C%EC%9D%B4%EC%8D%AC-2579-%EA%B3%84%EB%8B%A8-%EC%98%A4%EB%A5%B4%EA%B8%B0


# dp란? https://hongjw1938.tistory.com/47


# #런타임에러 ㅠ.ㅠ 빈배열에 append하는 방식
# import sys
# input = sys.stdin.readline
# arr = []
# dp = []

# l = int(input())
# for _ in range(l):
#     arr.append(int(input()))

# dp.append(arr[0])
# dp.append(max(arr[0]+arr[1],arr[1]))
# dp.append(max(arr[0]+arr[2],arr[1]+arr[2]))
# for i in range(3,l):
#     dp.append(max(dp[i-2] + arr[i] , dp[i-3] + arr[i] + arr[i - 1]))

# print(dp[-1])

# # range 범위 다름
# import sys
# input = sys.stdin.readline

# N = int(input())
# dp = [0 for _ in range(N+3)]
# arr = [0 for _ in range(N+3)]
# for k in range(1,N+1):
#     arr[k] = int(input())


# dp [1] = arr[1]
# dp [2] = arr[1] + arr[2]
# dp [3] = max(arr[1] + arr[3] ,arr[2] + arr[3])


# for i in range(4, N+1):
#     dp[i] = max( dp[i-3] + arr[i-1] + arr[i] ,  dp[i-2] + arr[i] ) 
# print(dp[N])