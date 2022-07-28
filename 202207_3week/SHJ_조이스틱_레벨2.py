'''
아스키 코드로 풀기
A: 97, Z:122

1. div = X - A(97)
   if div > 13:
      div = 26 - div (알파벳 25 + A->Z 이동할때 1)

'''
import  re

def getCount(s):
    div = ord(s) - ord("A")
    if div > 13:
        div = 26 - div
    
    return div

def solution(string):
    answer = 0

    for s in string:
        answer += getCount(s)

    # 한자리 숫자면 이동할 필요 없어서 바로 return
    if len(string) == 1:
        print(answer)
        return answer

    shift = 0
    # 13번 반례가 해결되지 않음.
    # # ABABAAAAABA: 좌우로 왔다갔다 하는 경우 
    if len(string) > 4 and string.find("A") >-1 :

        reString = re.sub('[B-Z]','B', string)
        
        Alist = reString.split('B')
        Alist.sort(reverse= True)
        # 붙어있는 A의 개수가 많으면 동작
        if len(Alist[0]) >= 2:
            n = len(Alist[0])
            idx = string.find(Alist[0])
            
            # AAAAA 기준 앞 문자 개수
            first = idx
            # AAAAA 기준 뒷 문자 개수
            last = len(string) - (n + idx) 
            
            if first <= 1:
                shift = last
            elif first > last:
                shift = last * 2 -1 + first
            else:
                shift = first *2 - 2 + last

    for i in range(1,len(string)):
        # BAACCCC -> 4번 이동 = 7(len) - 3(C index)
        if string[i]!="A" :
            if shift >(len(string) - i) or shift == 0:
                shift = (len(string) - i)
            break
    
    # BAAAAAA -> shift = 0
    for i in range(len(string)-1, 0,-1):
        # BBBBBAA -> 4번 이동 = 4(last B index)
        if string[i] != "A":
            if shift > i:
                shift = i
            break
    answer += shift
    
    print(answer)
    return answer


a = "JEROEN"
a = "ABABAAAAABA"
a = "BMOABA"
a = "BBBBAAAABBBABBBAAAB"
solution(a)
'''
반례
aa = []
aa.append("LAABAA              ".strip()) # answer:15
aa.append("AAAAAAAAJAAAA       ".strip()) # answer:14
aa.append("SAAAAAARRM          ".strip()) # answer:41
aa.append("RABAMATAWADLAFAVAAE ".strip()) # answer:78
aa.append("XAAAAAABA           ".strip()) # answer:6 
aa.append("AYOZAAVADAY         ".strip()) # answer:35
aa.append("AAFEASAAVA          ".strip()) # answer:30
aa.append("UAGAAASAAFAFXZA     ".strip()) # answer:47
aa.append("AAAAZAATAEA         ".strip()) # answer:19
aa.append("AACALATLAHABAA      ".strip()) # answer:50
aa.append("FAWJAAAFV           ".strip()) # answer:35
aa.append("AACAVAAPSAAOAA      ".strip()) # answer:49
aa.append("AKAAWAKX            ".strip()) # answer:33
aa.append("LOAAAHAJAAFAEBAWO   ".strip()) # answer:79
aa.append("AWAWVAQVAAA         ".strip()) # answer:35
aa.append("RCETAAAAVUEAETZAAAK ".strip()) # answer:75
aa.append("GTAASKKAE           ".strip()) # answer:52
aa.append("AAAABAAAAAAKSAIQ    ".strip()) # answer:49
aa.append("ADASAAAUAAAPAA      ".strip()) # answer:39
aa.append("AAAAADBAAELSPUAAAOA ".strip()) # answer:70
aa.append("VJAAIAFNAAAAA       ".strip()) # answer:47
aa.append("AARUAUAAHTBJAAYS    ".strip()) # answer:69
aa.append("IASAGITUPHE         ".strip()) # answer:74
aa.append("AAALAAAAAA          ".strip()) # answer:14
aa.append("AAAEASAHQAYTAAAJ    ".strip()) # answer:60
aa.append("BAALEAAAPMAAAHSRAV  ".strip()) # answer:83
aa.append("ASWAAATDAJAXA       ".strip()) # answer:45
aa.append("DYAOAAAARQANAWA     ".strip()) # answer:66
aa.append("AAIAPB              ".strip()) # answer:24

for c in aa:
    solution(c)
'''
