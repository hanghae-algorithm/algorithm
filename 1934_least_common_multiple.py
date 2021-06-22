# 주제 : 정수론 및 조합론
# 백준 코드 번호 : 1934
# 난이도 : 하
# 문제명 : 최소공배수
# 문제 설명 : 두 자연수 A, B가 주어졌을 때, A,B의 최소공배수를 구하라

# 해결방법(유클리드 호제법이 선이해되어야 함)
# 최대공약수(GCD) : a,b의 공통된 약수 중 가장 큰 약수
# 최소공배수(LCM) : a * b // 최대공약수
# import math를 해야 최대공약수인 math.gcd 사용가능
# 참고 링크 :
# 유클리드 호제법(https://velog.io/@chocho/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EC%9C%A0%ED%81%B4%EB%A6%AC%EB%93%9C-%ED%98%B8%EC%A0%9C%EB%B2%95)
# y 가 0이 되면 while문 탈출
# x = y,  y = x % y 요거 2개를 합쳐서 쓴거에요 x에는 y를 대입하고 y에는 x를 y로 나눈 나머지값 넣구요
# 유클리드호제법이 x를 y로 나눴을 때 나머지를 가지고 다시 그 나머지와 y로 동일하게 나머지를 계속 구해가는 거라 위의 식대로 표현한 것 같네요.
# 최종적으로 나머지가 0일 때 나눈 값이 gcd라 x를 반환했다고 보시면 될 것 같습니다

import math, sys

length = int(sys.stdin.readline()) 

for i in range(length): 
    a,b = map(int, sys.stdin.readline().split()) 
    a_b_gcd = math.gcd(a,b) 
    a_b_lcm = int(a * b / a_b_gcd)

print(a_b_lcm)


