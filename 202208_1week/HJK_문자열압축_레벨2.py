# https://school.programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    answer = s
    # 가능한 최대 단어 크기는 전체 문자열의 절반이다 
    # 예) 전체 10일때 길이5인 단어 2개가 있으면 압축 가능하나 길이6인 단어는 압축이 불가능하다
    max_size = len(s)//2    
    
    for size in range(1, max_size+1):
        s_copy = s
        compressed_s = ""
        cnt = 1

        # s_copy 에서 문자열만큼 제거하며 압축하며 compressed_s에 저장한다
        while(len(s_copy) >= size):
            word = s_copy[:size]
            s_copy = s_copy[size:]
            
            # 압축한 단어 뒷자리 size 만큼 가져와서 비교한다
            if compressed_s[-size:] == word:
                # 최근 단어와 현재 단어가 같으면 카운트 증가
                cnt += 1
            else:
                # 최근 단어와 현재 단어가 다르면 압축한 단어에 카운트를 추가한다
                # 문제에는 카운트가 단어 앞에 붙지만 문자열 길이에는 관계 없으므로 편의상 뒤에 붙인다
                if cnt > 1:
                    compressed_s += str(cnt) + word
                else:                    
                    compressed_s += word
                
                # 카운트 초기화
                cnt = 1            
        
        # 가장 마지막 카운트가 1보다 큼면 압축한 단어에 카운트를 추가한다
        if cnt > 1:
            compressed_s += str(cnt)
            
        # 남은 문자열이 있으면 압축한 문자열 젤 뒤에 붙인다
        if len(s_copy) > 0:
            compressed_s += s_copy
        
        # 기존 문자열 길이와 비교하여 짧은 것을 저장한다
        if len(answer) >= len(compressed_s):
            answer = compressed_s
    
    return len(answer)

s = "aabbaccc"
print(solution(s))