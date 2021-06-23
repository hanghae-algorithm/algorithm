# 문제 해설 https://leedakyeong.tistory.com/entry/%EB%B0%B1%EC%A4%80-1002%EB%B2%88-%ED%84%B0%EB%A0%9B-in-python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%BD%94%EB%93%9C-%EB%B0%8F-%EC%84%A4%EB%AA%85
# https://velog.io/@junyp1/%EB%B0%B1%EC%A4%80-1002-Python-%ED%84%B0%EB%A0%9B
# 고1 때 배운 원의 방정식에 대한 내용.
# 전체의 경우를 어떻게 알까? 특정 조건에서의 경우를 전체에서 어떻게 제외시킬까?
# 원이 두점에서 만나거나, 한점에서 만나거나, 겹쳐서 모든 원에서 만나거나, 만나지 않는다.


import sys, math
input = sys.stdin.readline

T = int(input())

for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = (math.sqrt(math.pow(x1-x2,2) + math.pow(y1-y2,2)))
    # distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5         #위 식과 동일한 결과
    # m = list([r1, r2, distance])     아래 else문 안 if문에 max(m)과 sum(m)을 쓰기위한 리스트

    if distance == 0:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    

    else: 
        if distance > r1+r2 or distance < abs(r1-r2):
        # if max(m) > sum(m) - max(m):                위에 or 조건을 바꿔쓴 경우
            print(0)
        
        
        elif distance == r1+r2 or distance == abs(r1-r2):
            print(1)
        

        else:
        # elif distance < r1+r2 and distance > abs(r1-r2):  # and 조건이 아닐 경우 안만나거나 1점만 만날 수도 있음
            print(2)




# T = int(input())
# for i in range(T):
#     A=list(map(int,input().split()))
#     dist = ((A[0]-A[3])**2 + (A[1]-A[4])**2)**(1/2)
#     if dist == 0:
#         if A[2]==A[5]:
#             print(-1)
#         else:
#             print(0)
#     elif dist < abs(A[2]-A[5]):
#         print(0)
#     elif dist == abs(A[2]-A[5]):
#         print(1)
#     elif A[2]+A[5] < dist:
#         print(0)
#     elif A[2]+A[5] == dist:
#         print(1)
#     else:
#         print(2)
# https://curihus.tistory.com/11