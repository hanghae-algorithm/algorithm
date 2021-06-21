# # 작성일 : 21-06-21
# # 주제 : 큐, 덱
# # 난이도 : 하
# # 담당자 : 윤송
#
# # 백준 코드번호 : 18258
# url: https://www.acmicpc.net/problem/18258
# # 문제명 : 큐 2
# # 문제설명 : 큐 구현하기
# # 해결 방법
#   Linked List를 이용하여 큐를 구현하였다.
# 참고 : 백준 pypy로 진행


import sys

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # 맨뒤에 데이터 추가
    def push(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
        else:
            # 왜 self.tail.next에도 노드를 추가할까?
            self.tail.next = new_node
        self.size += 1
        self.tail = new_node

    def pop(self):
        if self.is_empty():
            return -1

        temp = self.head
        self.head = self.head.next
        self.size -= 1
        return temp.data

    def get_size(self):
        return self.size

    def is_empty(self):
        return 1 if self.head is None else 0

    def front(self):
        if self.is_empty():
            return -1
        return self.head.data

    def back(self):
        if self.is_empty():
            return -1
        return self.tail.data


n = int(input())
queue = Queue()

for _ in range(n):
    msg = list(sys.stdin.readline().split())

    if msg[0] == 'push':
        queue.push(msg[1])
    elif msg[0] == 'pop':
        print(queue.pop())
    elif msg[0] == 'size':
        print(queue.get_size())
    elif msg[0] == 'empty':
        print(queue.is_empty())
    elif msg[0] == 'front':
        print(queue.front())
    elif msg[0] == 'back':
        print(queue.back())
