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


import math, sys

length = int(sys.stdin.readline()) 

for i in range(length): 
    a,b = map(int, sys.stdin.readline().split()) 
    a_b_gcd = math.gcd(a,b) 
    a_b_lcm = int(a * b / a_b_gcd) 
    print(a_b_lcm)


