# https://kongpowder.tistory.com/78
# #배열 사용하기
# n = int(input())
# a = []
# cnt = 0 
# for i in range(n):
#     s = list(map(str, input()))
#     flag = False
#     a = []
#     for j in range(len(s)):
#         if s[j] not in a :
#             a.append(s[j])
#         else :
#             if s[j-1] != s[j]:
#                 flag = True
#     if flag == False:
#         cnt += 1
# print(cnt)






# # https://aisiunme.github.io/algorithm/2018/08/13/baekjoon-group-word-checker-1316.md/
# # 그룹 단어 0부터 세기
# n = int(input())
# result = 0
# for i in range(n):
#     word = input()
#     if list(word) == sorted(word, key=word.find):
#         result += 1
# print(result)

# https://namhandong.tistory.com/67
# 인풋값에서 그룹 단어 아닌 것 빼기  
# find는 해당하는 단어를 찾아서 index를 알려주는데 따로 값을 지정하지 않으면 첫번째 위치를 알려준다.
# 만약 앞에 있는 단어의 find index가 뒤에 있는 단어의 find index 보다 크다면 그룹단어가 아니다.
# 예를 들어 aba라는 단어에서 b는 index가 1/ a는 index가 0인데 .find(word[2])는 0, .find(word[1])은 1이므로 그룹단어가 아니다.


# N=int(input())
# count=N

# for _ in range(N):
#     word=input()
#     for i in range(len(word)-1) :
#         if word.find(word[i]) > word.find(word[i+1]):
#             count -=1
#             break
# print(count)



N = int(input())
count = N

for i in range(N):
    0
    1
    2
    print(i)


#     word = input()
#     for j in range(len(word)-1):
#         if word.index(word[j]) > word.index(word[j+1]):
#             count -= 1
#             break

# print(count)
