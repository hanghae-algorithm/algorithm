# 간단하게 정리해서 풀이 한 것 https://wiselog.tistory.com/126
# 새로나온 개념 deque > 큐의 앞과 뒤에서 삽입과 삭제가 가능하다. 스택처럼 또는 큐처럼 사용할 수 있다.
# 시작점의 값을 넣고 빼거나, 끝 점의 값을 넣고 빼는 데 최적화된 연산 속도를 제공한다.
# 즉, 대부분의 경우 덱(deque)이 리스트(list)보다 월등한 옵션이다.
# 해당 예시에서 리스트에서는 불가능한 deque에서는 appendleft, popleft가 가능

# 1. 큐 중에서도 양쪽으로 삽입삭제가 가능한 덱(deque)을 사용했다.
# 2. 인덱스(1부터)만 주어지고, 각 인덱스의 값은 몰라도 되므로, 편하게 계산하기 위해 각 인덱스를 값으로 가지는 큐 dq를 만들어 사용했다.
# 3. 입력받은 인덱스를 저장한 배열 idxs를 탐색한다.
# 4. idxs의 원소 idx가 큐에서 제거될 때까지 반복한다.
#   4-1. dq의 맨 앞 원소가 현재 idx와 같다면, 제거 후 break
#   4-2. 같지 않다면, dq에서의 idx의 위치를 알아낸다.
#     4-2-1. 위치가 dq의 앞쪽이라면, 앞 원소를 빼서 뒤로 보내는것이 빠르므로, idx가 dq의 맨 앞으로 올 때까지 문제의 2번 연산(왼쪽으로 한 칸 이동시킨다.) 수행 후 count 1 증가
#     4-2-2. 위치가 dq의 뒤쪽이라면, 뒤 원소를 빼서 앞으로 보내는것이 빠르므로, idx가 dq의 맨 앞으로 올 때까지 문제의 3번 연산(오른쪽으로 한 칸 이동시킨다.) 수행 후 count 1 증가
#     4-2-3. 여기서 신경써야 할 점은, dq의 길이가 홀수일 때는 중간 인덱스까지 앞으로 돌리는 것이 빠르므로, (dq의 길이/2)값이 자동 내림되지 않도록 해야한다. (1 2 3 4 5 일때, 1 2 3은 앞으로, 4 5는 뒤로)



from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
idxs = list(map(int, input().split()))
# dq = deque([i for i in range(1, n+1)])  ##???? 다른 형식으로 사용못하나
dq = deque(range(1, n+1))             ## 이것처럼 써도 같은 결과 같은 값인데 왜 이렇게쓴지 모르겠다.
count = 0
for idx in idxs:                        ##2, 9, 5 차례대로 들어감
    while True:
        if dq[0] == idx:                #방금 들어간 값이 dq[0]번째라면
            print(dq,'dq[0]==idx')
            dq.popleft()                #dq에서 방금 것(dq[0]) 삭제
            
            break
        else:
            if dq.index(idx) < len(dq)/2:  # idx가 dq의 앞에 위치할 경우 왼쪽으로 이동시킨다.
                while dq[0] != idx:
                    print(dq,'dq.index(idx) < len(dq)/2')
                    dq.append(dq.popleft())   #-> 왼쪽으로 이동
                    count += 1
                    
            else:
                while dq[0] != idx:        # idx가 dq의 뒤에 위치할 경우 오른쪽으로 이동시킨다.
                    print(dq, 'dq.index(idx) >= len(dq)/2')
                    dq.appendleft(dq.pop())  # -> 오른쪽으로 이동
                    count += 1
                    
print(count)
print(dq, '마지막 dq의 모양새')


# import sys
# from collections import deque
# n, _ = map(int, sys.stdin.readline().split())
# numbers = list(map(int, sys.stdin.readline().split()))
# queue = deque(range(1, n+1))
# total_compute = 0

# for i in range(len(numbers)):
#     if numbers[i] == queue[0]:
#         print(queue, '원하는 위치')
#         queue.popleft()
#         continue
#     queue_i = queue.index(numbers[i])

#     #뒤에있는 경우 > 우측으로 이동해야 한다.
#     if queue_i > len(queue) // 2:
#         print(queue, 'queue 전체 우측 이동')
#         queue.rotate(len(queue) - queue_i)
#         total_compute += (len(queue)- queue_i)

#     #앞에 있는 경우 > 좌측으로 이동해야 한다.
#     elif queue_i <= len(queue) // 2:
#         print(queue, 'queue 전체 좌측 이동')
#         queue.rotate(-queue_i)
#         total_compute += queue_i   # >1
#     queue.popleft()

# print(total_compute)

# 출처 : https://inspirit941.tistory.com/176


##ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ아래부터는 비슷한 다른 풀이들 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# from collections import deque
# import collections
# n, m = map(int, input().split())
# target = deque(map(int, input().split()))
# q = deque([x for x in range(1, n+1)])
# cnt = 0
# while len(target):
#     t = target.popleft()
#     t_point = q.index(t)
#     if t_point != 0:
#         if len(q)-t_point > t_point:
#             q.rotate(-t_point)
#             cnt += t_point
#         else:
#             q.rotate(len(q)-t_point)
#             cnt += len(q)-t_point
#     q.popleft()
# print(cnt)

# 출처: https://binux.tistory.com/48 [개발을 부시다]



# from collections import deque
# n,m = list(map(int,input().split()))
# value = list(map(int,input().split()))
# q = deque([i+1 for i in range(n)])
# count = 0
# for x in value:
#     while True:
#         if q.index(x) == 0:
#             q.popleft() # 1번 로직 break # 위치 0과의 거리 차이로 왼쪽으로 이동할 지 오른쪽으로 이동할 지를 결정
#             if q.index(x) - 0 <= len(q) - q.index(x): # 2번 왼쪽으로 이동하기 로직
#                 q.append(q.popleft())
#                 count += 1
#             else: q.appendleft(q.pop()) # 3번 오른쪽으로 이동하기 로직
#             count += 1
# print(count)

# 출처: https://seongbindb.tistory.com/57 [SeongbinDB]



