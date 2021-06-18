# #1.
import sys

N = int(sys.stdin.readline())

stack = list()

for i in range(N):
    cmd = sys.stdin.readline().split()

    if cmd[0] == "push":
        stack.append(int(cmd[1]))  # push 1

    elif cmd[0] == "pop":
        if not stack:
            print('-1')
        else:
            print(stack[-1])  # 제일 마지막으로 들어온 수가 먼저 나간다
            stack.pop()

    elif cmd[0] == "size":
        print(len(stack))

    elif cmd[0] == "empty":
        if not stack:
            print(1)
        else:
            print(0)

    elif cmd[0] == "top":
        if not stack:
            print(-1)
        else:
            print(stack[-1])


# 2.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        new = Node(value)
        if self.head == None:
            self.head = new
            return
        else:
            old = self.head
            self.head = new
            new.next = old
            return

    def pop(self):
        if self.head == None:
            print(-1)
            return -1
        out = self.head  # 가장 위에 있는 정수를 뺀다
        self.head = out.next  # 다음 노드가 self.head가 된다.
        print('test', out.next.data)
        out.next = None  # 기존의 셀프 헤드 다음 노드를 지워준다.
        print(out.data)
        return self.head

    def top(self):
        if self.head == None:
            print(-1)
        else:
            db = self.head
            print(db.data)
            return

    def isEmpty(self):
        if self.head == None:
            print(1)
            return 1
        else:
            print(0)
            return 0

    def size(self):  # 개수
        if self.head == None:
            print(0)
        else:
            count = 1
            db = self.head
            while db.next != None:
                db = db.next
                count += 1
            print(count)
            return


stack = Stack()

import sys

key = sys.stdin.readline().rstrip()
key = int(key)

for i in range(key):
    command = list(sys.stdin.readline().split())
    if command[0] == "push":
        data = stack.push(int(command[1]))  # push 1이 명령어임

    if command[0] == "top":
        data = stack.top()

    if command[0] == "size":
        data = stack.size()

    if command[0] == "empty":
        stack.isEmpty()

    if command[0] == "pop":
        stack.pop()

