# # 작성일 : 21-06-18
# # 주제 : 이분탐색
# # 난이도 : 중
# # 담당자 : 윤송
#
# # 백준 코드번호 : 2805
# # 문제명 : 나무자르기
# # 문제설명 : 일렬로 있는 나무들을 한꺼번에 자를 때 절단기 위치보다 높은 나무들만 잘릴 것이고 낮은 나무들은 잘리지 않을 것이다.
#             만약 M미터의 나무를 가져가고 싶다면 절달기를 놓을 위치를 구하랑
#
# # 해결 방법
# # 변수 정리
# # height : 절단된 나무 길이
# # length_required : 요구된 나무 길이
# # cutter : 절단기 높이
#

# 해결 전 생각할 것
# 1. 톱날의 높이가 낮을 수록 더 많은 나무를 벨 수 있다.
# 2. 문제 '톱날의 높이'를 Binary Search를 이용하여 찾아 나간다.
# 3. 톱날의 높이가 결정되었을 때, height 미터보다 크거나 같으면, 톱날의 높이 cutter를 높여준다. (같을 때 톱날의 높이를 높여주는 것이 핵심.)
# 4. M미터보다 작으면, 톱날의 높이 H를 낮춰준다.
# 참고 출처 : https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=pjok1122&logNo=221652208967


import sys

count, length_required = map(int, input().split())
trees = list(map(int, sys.stdin.readline().split()))
start = 0
end = max(trees)


# '시간초과'를 방지하기 위해 while문에 포함하지않고 함수를 따로 빼놓음
# 절단기 높이 구하는 함수
def tree_height(cutter):
    height = 0
    for tree in trees:
        if tree - cutter > 0:
            height += (tree - cutter)
    return height


while start <= end:
    cutter = (start + end) // 2
    height = tree_height(cutter)
    print(f'start: {start}, end: {end}, cutter: {cutter}, height: {height}', 'test')
    # 만약 절단된 나무가 요구된 길이보다 짧다면 절단 높이를 낯줘준다.
    if height < length_required:
        end = cutter - 1
    # 만약 절단된 나무가 요구된 길이보다 길다면 절단 높이를 높혀준다.
    elif height >= length_required:
        answer = cutter
        start = cutter + 1

    # 절단된 나무길이와 요구된 나무길이가 동일할 때 까지 반복한다.
    if height == length_required:
        break

print(answer)

# # 변수 정리
# # height : 절단된 나무 길이
# # length_required : 요구된 나무 길이
# # cutter : 절단기 높이
#
# import sys
#
# count, length_required = map(int, input().split())
# trees = list(map(int, sys.stdin.readline().split()))
# trees.sort()
# # 가운데 나무를 기준으로 시작
# mid_index = count // 2
# cutter = trees[mid_index]
# height = 0
# while True:
#     height = 0
#     for tree in trees:
#         n = tree - cutter
#         if n >= 0:
#             height += n
#
#     # 만약 절단된 나무가 요구된 길이보다 짧다면 절단 높이를 낯줘준다.
#     if height < length_required:
#         cutter -= 1
#     # 만약 절단된 나무가 요구된 길이보다 길다면 절단 높이를 높혀준다.
#     elif height > length_required:
#         cutter += 1
#
#     # 절단된 나무길이와 요구된 나무길이가 동일할 때 까지 반복한다.
#     if height == length_required:
#         break
#
# print(cutter)
