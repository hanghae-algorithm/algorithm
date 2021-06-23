# 문제 : 백준 2798 블랙잭
# 주제 : 브루트포스
# 난이도 : 중
# 문제 설명 : N장의 카드 중 3장을 뽑아 그 합이 M을 넘지 않고 최대한 M과 가까워야 한다.

# 1
N, M = map(int, input().split())
cards = list(map(int, input().split()))
result = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            print('test', i, j, k)
            if cards[i] + cards[j] + cards[k] <= M:
                result = max(result, cards[i] + cards[j] + cards[k]) # 현재 result와 비교해서 result에는 항상 큰 값이 담길 수 있도록 한다.

print(result)

# 2 (출처: https://wonjongah.tistory.com/74?category=915051)
# combination : 서로다른 n개 중에서 r개를 취한 조합. 순서를 고려하지 않기 때문에 (A, B) = (B, A)로 취급

from itertools import combinations

n, m = list(map(int, input().split()))
card_num = list(map(int, input().split()))

# 카드의 순열을 구한다.
card_cases = list(combinations(card_num, 3))
# 각 케이스마다의 합을 저장한다.
summary = []

# 각 카드의 순열의 합이 m보다 크면 다음 카드 순열을 불러오고,
# 작거나 같다면 합의 배열에 추가한다.
for case in card_cases:
    if sum(case) > m:
        continue
    else:
        summary.append(sum(case))

# 각 합의 제일 큰 값을 리턴한다.
print(max(summary))