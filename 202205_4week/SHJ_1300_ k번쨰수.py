# 1300번 k번째수

# 문제
# 세준이는 크기가 N×N인 배열 A를 만들었다. 배열에 들어있는 수 A[i][j] = i×j 이다. 이 수를 일차원 배열 B에 넣으면 B의 크기는 N×N이 된다. B를 오름차순 정렬했을 때, B[k]를 구해보자.

# 배열 A와 B의 인덱스는 1부터 시작한다.

# 입력
# 첫째 줄에 배열의 크기 N이 주어진다. N은 105보다 작거나 같은 자연수이다. 둘째 줄에 k가 주어진다. k는 min(109, N2)보다 작거나 같은 자연수이다.

# 출력
# B[k]를 출력한다.

# 예제 입력 1 
# 3
# 7
# 예제 출력 1 
# 6

def get_cnt(mid, n):
    l = [min(mid // i, n) for i in range(1,n+1)]
    return sum(l)

def main(n:int, k:int):
    s, e = 1, k # l[k] <= k
    mid = 0     # 숫자
    while s <= e:
        mid = (s+e)//2      
        idx = get_cnt(mid, n)  # 인덱스 (=개수)

        if idx >= k:
            answer = mid       # 이것의 의미는 ..?? 마지막 변경은 반영하지 않음 + idx >= k일때의 값만 반영
            e = mid-1
        else:
            s = mid+1
    return answer

if __name__ == "__main__":
    n = int(input())        # 굴다리의 길이
    k = int(input())        # 가로등의 개수
    
    result = main(n, k)
    print(result)