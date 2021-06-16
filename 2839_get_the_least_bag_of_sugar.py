# 작성일 : 21-06-16
# 주제 : 기본 수학 1
# 난이도 : 하

# 문제명 : 설탕 배달
# 문제설명 : 3kg과 5kg의 설탕봉지가 있다. N킬로그램의 설탕을 배달하기 위해
#           3kg과 5kg가 합쳐진 최소 봉지 개수를 구하라
# 백준 코드번호 : 2839
# # 배운점
# 반복문을 써야한다는 것을 알았지만 솔직히 구글링하기 전까지 while문이 아닌 for문에 집착하고 있었다.
# 한가지 방법에만 익숙해진 나머지 다른 방법은 생각도 못했다. 다양한 기능들을 활용할 수 있도록 의식적으로 노력해야겠다.

sugar_kg = int(input())
total_bag = 0
# 주어진 값이 0이 될 때까지 while 문 진행
while sugar_kg != 0:
    if sugar_kg % 5 == 0:
        # Case1. 설탕의 무게가 5의 배수라면 5kg 봉지로 계산 후 루프 종료
        total_bag = (sugar_kg / 5) + total_bag
        break
    elif sugar_kg % 5 != 0 and sugar_kg % 3 != 0 and sugar_kg < 3:
        # Case2. 설탕의 무게가 3과 5의 배수가 아니며 3 미만일 경우 계산이 불가하므로 -1 반환
        total_bag = -1
        break

    sugar_kg -= 3   # 설탕의 무게가 5의 배수가 아닐 경우 3kg 봉지로 계산
    total_bag += 1

print(int(total_bag))
