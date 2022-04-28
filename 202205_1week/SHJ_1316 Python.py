# 1316번 그룹단어 체어
# 39780 kb
# 184 ms

# aabbccb
# {a: 0, 1}
# {b: 2, 3, 6}
# {c: 4, 5}
# max - min = length -1 -> 그룹단어 조건 충족
# max - min != length -1 -> break, 입력받은 숫자 -1

from ast import Return
import math
from pickle import LIST

n = input()         # 데이터 셋 개수
iN = int(n)         # int 타입 변환

for i in range(iN):
    ch = input()    # 문자열 입력 받음
    
    dic = {}
    g_cnt = 0
    for i in range(len(ch)):        # 문자열 길이만큼 반복
        if ch[i] in dic:            # 리스트에 인덱스 추가
            dic[ch[i]].append(i)
        else:                       # 최초 입력시 리스트로 인덱스 추가
            dic[ch[i]] = []
            dic[ch[i]].append(i)
    
    
    for key, value in dic.items():
        length = len(value)         # a의 index 개수

        if length > 1:              # 개수가 1이면 그룹단어. 이상이면 체크 필요함
            iMax = int(max(value))  # 인덱스 최대값
            iMin = int(min(value))  # 인덱스 최소값
            
            if iMax - iMin != (length-1): # 최대값 - 최소값 != 길이 -1 -> 그룹문자  ex) 2, 3, 4 -> 4-2 = 2, 길이는 3
                iN = iN - 1               # 그룹문자가 아닌 경우 개수 차감하고 다음 문자로 넘어감
                break
        
print(iN)
