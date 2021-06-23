n = int(input())            #입력값 입력
result = 0                  #입력값 n과 비교하기 위한 변수
for i in range(1,n+1):
    a = list(map(int,str(i)))  #str함수를 통해 i의 각 자리수를 a 리스트에 넣기
    result = i + sum(a)        #예제를 봤을 때, 분해합은 256(=245+2+4+5)이므로 i값에 각 자리수가 들어간 a리스트의 합을 더해준다.
    if result == n:            #합을 더한 것과 n비교
        print(i)
        break
    if i == n:                 #생성자가 없는 경우 0을 출력
        print(0)



# n = int(input())
# result = 0
# for i in range(1,n+1):
#     a = list(map(int,str(i)))
#     b = i + sum(a)
#     if b == n:
#         result = i
#         break
#
# print(result)

