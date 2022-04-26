# 문제 
# 그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다. 예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만, aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.
# 단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.

# 첫번째 라인 입력은 단어의 갯수 100보다 작거나 같은 자연수 
n = int(input())
# 둘째 줄부터 N개의 줄에 단어가 들어온다. 단어는 알파벳 소문자로만 되어있고 중복되지 않으며, 길이는 최대 100이다.
words = [input() for _ in range(n)]

# 그룹단어의 갯수, 입력 단어와 동일한 숫자로 시작하여 차감한다
cnt = n
# 중복되는 알파벳 누적
chr_list = []

for word in words:
    chr_list.clear()

    for j in word:
        
        if len(chr_list) == 0:
            # 가장 최근 알파벳을 0 인덱스로 부터 쉽게 찾아오기 위해 list 앞쪽에 추가 한다
            chr_list.insert(0, j) 

        elif chr_list[0] == j:
            # 알파벳이 이어지면 건너뛴다
            pass

        elif (j not in chr_list):
            # 새로운 알파벳은 추가한다
            chr_list.insert(0, j)

        else:
            # 이어지지 않는 기존 알파벳이 있으면 차감하고 빠져나간다
            cnt -= 1
            break

print(cnt)