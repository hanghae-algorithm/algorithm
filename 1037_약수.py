# 1037
# 문제 : N의 진짜 약수가 주어질 때, N을 구하기
# 진짜 약수 : 1과 N을 제외한 N의 악수

# 1번 풀이
N = int(input())
a = list(map(int, input().split()))

max_num = max(a)
min_num = min(a)

print(max_num * min_num)

# 2번 풀이
N = int(input())
a = list(map(int, input().split()))

a.sort() # a.sort(): 오름차순 정렬, a.sort(reverse = True) : 내림차순 정렬
print(a[0] * a[-1])
