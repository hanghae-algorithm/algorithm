# 작성일 : 21-06-15
# 주제 : 문자열
# 난이도 : 하

# 문제명 : 그룹 단어 체커
# 문제설명 : 그룹단어란 문자가 연속해서 나타나는 경우를 말한다. 주어진 input값 중 그룹단어의 개수를 반환해라
# 백준 코드번호 : 1316

# 배운점
# 1. 전날 풀다가 안되어서 잠시 접었던 문제인데 오늘 아침에 다시 푸니 구현이 잘 되었다.
#     + 노트에 전체적인 틀 그려보기!! 도움이 되었다.
#    역시 안되는 문제 계속 붙잡고 있는 거 보단 다른 쪽으로 잠깐 눈을 돌리는 것도 방법이라고 생각한다. 특히 프로그래밍할 때는
#     비슷한 맥락이기에 다른 곳에서 반대로 아이디어를 얻을 수 있으므로
# 2. input 값을 받을 때 input()으로 싱글단어, input().split로 다중값을 받을 수 있다.


lists_count = int(input())
is_not_group_word_count = 0

for i in range(lists_count):
    input_value = input().split()[0]

    temp = ""
    char_arr = []

    for char in input_value:            # 1. 단어안에 글자 수만큼 루프를 돌며
        if char != temp:                # 2. 글자가 바뀔 때 마다 배열에 해당 글자를 넣어주고
            if char in char_arr:        # 3. 만약에 이미 동일한 글자가 저장되어있다면 그룹단어가 아니므로 카운트 변수는 업
                is_not_group_word_count += 1
                break                   # 4. 루프를 종료 시킨다.
            else:
                char_arr.append(char)
        temp = char

print(lists_count - is_not_group_word_count)  # 5. 전체 단어 개수에서 그룹단어가 아닌 수를 빼면 그룹 단어의 수가 출력된다.



