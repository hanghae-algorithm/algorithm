# 문제 번호 : 2108
# 문제명: 통계학
# 주제 : 정렬
# 난이도 : 중
# 참고 링크 : https://somjang.tistory.com/entry/BaekJoon-2108%EB%B2%88-%ED%86%B5%EA%B3%84%ED%95%99-Python (풀이 참고)
# counter : https://velog.io/@kimdukbae/Python-collections-%EB%AA%A8%EB%93%88%EC%9D%98-Counter
# 문제설명: 산술평균, 중앙값, 최빈값, 범위. 4가지 기본 통계값을 구하는 프로그램 작성

from collections import Counter
import sys

numbers = []
for _ in range(int(sys.stdin.readline())):
    num = int(sys.stdin.readline())
    numbers.append(num)

numbers.sort()

print(round(sum(numbers) / len(numbers)))  # 산술평균 : 반올림 rount()
print(numbers[len(numbers) // 2])  # 중앙값 : 반으로 나눴을 때 중앙에 위치하는 값(몫)

# 최빈값
# counter.most_common(2) < 빈도수 상위 2개를 튜플 자료형으로 가져온다.
# 예시: [('kim', 5), ('choi', 3)] - > [('값', 개수)] 형식
# 1) 길이가 1이면 하나밖에 없으니 바로 프린트한다.
# 2) 길이가 1보다 크다면, 두 요소의 벨류 값을 비교했을때 같다면 두번째로 작은 값을 가져온다.

cnt = Counter(numbers).most_common(2)
print(cnt)
if len(numbers) > 1:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])  # key값을 가져와야 함.
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])

print(max(numbers) - min(numbers))  # 범위
