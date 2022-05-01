"""문제
어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다. 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오. 

입력
첫째 줄에 1,000보다 작거나 같은 자연수 N이 주어진다.

출력
첫째 줄에 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력한다."""

n = int(input())

# 1~n 까지 반복하기 위해 1부터 시작
i = 1
# 한수의 갯수
cnt = 0

# 한수인 경우 True
def isHanSu(a):
    # 두 자리수 이하는 한수
    if int(a) <= 99:
        return True
    
    # 직전수
    p = -1
    # 직전수와 차이
    d = None

    for j in a:
        # 첫번째 자릿수일 경우 패스
        if p == -1:
            pass
        else:
            # d 는 한번만 기록하면 된다.
            if d is None:
                d = int(j) - p
            else:
                # 이전수와 차이가 d 와 다르면 한수가 아님
                if (int(j) - p) != d:
                    return False
        p = int(j)
    
    return True

for i in range(n):
    # 한수인지 체크해서 한수이면 카운터 1증가
    if isHanSu(str(i+1)):
        cnt += 1

print(cnt)