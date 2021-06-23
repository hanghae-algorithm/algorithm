### https://st-lab.tistory.com/75 참고
import math, sys
a, b, v = map(int, input().split())    # 한줄에 여러 변수 넣을 때             
# a,b,v = map(int,sys.stdin.readline().split())     #tmi.반응속도를 줄이기 위해 여기와 바로 윗줄을 비교해서 제출해본 결과 반응속도가 똑같이 나왔다. 아마도 여러 줄 입력할 때 반응속도의 차이가 나올듯
# a, b, v = map(int, input().split())               
# v = day(a) - (day - 1)*b                          # 달팽이가 매일마다 미끄러지지만 정상에서는 미끄러지지 않으므로 마지막날은 -b를 할필요가 없다. 
# v = day(a-b)+b                                    # day에 대하여 우항을 묶었다.
# v-b = day(a-b)                                    # +b를 좌항으로 이동시켰다.(양변에 -b)
# day = v-b/a-b                                     # 양변을 a-b로 나누고 좌항과 우항을 바꿨다.
day = (v - b) / (a - b) + 1                         # 정리되어 나온 day의 값. 정수 또는 실수, 실수가 나올 경우 달팽이가 하루 더 올라야 정상에 닿기 때문에 올림을 쓴다.
print(math.ceil(day))   # import math할 시 쓸 수 있는 올림! math() 괄호 안의 수를 올림한다.




# ### 처음 생각해서 while로 풀어 본 결과 >> 시간초과가 난다.##
a, b, v = map(int, input().split())
height = 0
day = 0

while height < v-a:       #달팽이가 정상에 오르기 전까지 반복하라
    height += a-b
    day += 1
print(day+1)              # day가 정상에 오르기 바로 전날 이기 때문에 1을 더해서 출력