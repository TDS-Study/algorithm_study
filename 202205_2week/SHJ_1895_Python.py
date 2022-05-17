# 1895번 필터
# 메모리  KB
# 시간  ms

def filter(r, c):
    sample = [] # 3x3을 1차원으로 입력
    for ir in range(r, r+3):
        for ic in range(c, c+3):
            sample.append(img[ir][ic]) 

    sample.sort()    # 오름차순 정렬
    return sample[4] # 중앙값 반환

img = []

r, c=map(int, input().split(' ')) # r: 이미지 세로 픽셀수, c: 이미지 가로 픽셀수

# 픽셀 값 저장
for iR in range(r): 
    img.append(list(map(int, input().split(' '))))

t = int(input()) # 기준 값
over_t = 0       # t보다 큰 값의 개수

for iR in range(r-2):
    for iC in range(c-2):
        filtered_v = filter(iR, iC)
        if filtered_v > t:
            over_t = over_t+1

print(over_t)