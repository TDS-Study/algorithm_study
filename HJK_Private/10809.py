"""문제
알파벳 소문자로만 이루어진 단어 S가 주어진다. 각각의 알파벳에 대해서, 
단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 
포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 단어 S가 주어진다. 단어의 길이는 100을 넘지 않으며, 알파벳 소문자로만 이루어져 있다.

출력
각각의 알파벳에 대해서, a가 처음 등장하는 위치, 
b가 처음 등장하는 위치, ... z가 처음 등장하는 위치를 공백으로 구분해서 출력한다.

만약, 어떤 알파벳이 단어에 포함되어 있지 않다면 -1을 출력한다. 
단어의 첫 번째 글자는 0번째 위치이고, 두 번째 글자는 1번째 위치이다."""

wrd = input()
# 결과 저장 리스트
result = []
# a 의 아스키 코드
offset = ord('a')

# z-a 아스키 차이 만큼 돌면서 a-z 까지 확인
for i in range(int(ord("z"))-int(ord("a"))+1):
    # 끝까지 돌고 못찾은 경우를 위해 flag를 둔다
    isFound = False
    
    for j in range(len(wrd)):
        if chr(offset+i) == wrd[j]:
            # 찾은 경우 위치를 추가하고 빠져나간다
            result.append(j)
            isFound = True
            break

    # 못찾은 경우 -1 추가
    if isFound == False:
        result.append(-1)

# 리스트를 공백을 추가하여 출력한다
# print(' '.join([str(i) for i in result]))
rst = ""

for i in result:
    rst += str(i) + " "

# 마지막 공백 제거
rst = rst[0:len(rst)]

print(rst)