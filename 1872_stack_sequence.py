# 문제 : 백준 1874
# 주제 : 스택 - 스택 수열
# 문제 설명 : 임의의 수열(push순서는 반드시 오름차순)이 주어졌을 때 스택을 이용해서 수열을 만들 수 있는지 없는지, 있다면 어떤 순서로 pop과 push 연산을 수행해야 하는지 계산하라.
# (push 연산은 +로, pop 연산은 -로 표현한다. 불가능하면 no를 출력하라)
# 참고링크 : https://wookcode.tistory.com/31
# https://velog.io/@kgpaper/%EB%B0%B1%EC%A4%80-1874%EB%B2%88-%EC%8A%A4%ED%83%9D-%EC%88%98%EC%97%B4

# 해설
# pop에서 첫 번째 인자를 꺼내고 싶다면 pop(0)으로 지정해줘야 한다. 아니면 스택처럼 가장 마지막에 들어온 인자를 꺼낸다.
# n에 8이 들어갔기 때문에 1-8까지의 수를 스택에 넣었다가 뽑아서 수열을 만든다.
# 처음에 4를 넣게 되면 스택에 1,2,3,4 를 넣게 되고 4를 빼준다.
# 다음에 3이 들어오면 count 보다 작아서 while 문에 들어가지 않고 스택의 맨 위값과 입력값이 같기 때문에 바로 pop를 해준다.

# count <= a : 현재 수열의 원소가 나올때까지 스택에 카운트를 추가함.(push)
# stack[-1] == a: 스택에서 원소를 빼줌(pop)
# count > a : 스택의 마지막 원소가 더 클 경우는 False. (가장 마지막에 들어온 원소가 가장 먼저 나간다)


n = int(input())
stack = []
result = []
count = 1
boolean = True

for i in range(n):
    a = int(input())
    while count <= a:
        stack.append(count)
        result.append('+')
        count += 1

    if stack[-1] == a:
        stack.pop()
        result.append('-')

    else:
        boolean = False
        break

if boolean == False:
    print('NO')
else:
    for i in result:
        print(i)
