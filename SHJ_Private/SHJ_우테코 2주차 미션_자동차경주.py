'''
 자동차들끼리 경주하여 최종 우승자를 출력하는 게임을 구현합니다.

​

1. 입력

[자동차]

- 자동자이름을 쉼표로 구분하여 입력받습니다.

- 자동차 이름은 5자 이하여야 합니다.

[시도 횟수]

- 양수를 입력받습니다.

​

2. 실행

[전진 조건]

- 각 자동차는 랜덤으로 0~9사이에 값을 만든 후 값이 4 이상일 경우만 전진합니다

​

3. 출력

- 자동차들이 라운드를 끝냈을 때마다 실행결과를 출력합니다.

- 시도 횟수만큼의 라운드가 끝난 후에 최종 우승자를 출력합니다. (2명 이상일 경우에는 ,쉼표로 구분하여 출력)

​

4. 기타 사항

[Exception]

- 사용자의 입력이 잘못되었을 경우에 IllegalException을 발생시키며, 에러메시지를 출력하고 다시 입력받습니다.

[구현]

- 자바 코드 컨벤션을 지킨다.

- indent는 2이하

- else 예약어를 사용하지 않는다.

- 함수는 한가지 기능만 하게 구현

- 프로그래밍 요구사항에서 별도로 변경 불가 안내가 없는 경우, 파일 수정과 패키지 이동을 자유롭게 할 수 있다.
[출처] [우테코]2주차 미션 회고록: 자동차 경주 게임|작성자 여름나무
'''

from multiprocessing.sharedctypes import Value
import random
print("경주할 자동차 이름을 입력하세요(이름은 쉼표 기준으로 구분함)")
cars = list(input().split(','))
act = {}
print("시도할 회수는 몇회인가요?")
round = int(input())
winner_score = 0

for car in cars:
    act[car] = ""
    
for _ in range(round):
    print("실행결과",str(_+1))
    for car in cars:
        number = random.randint(0,9)
        if number >= 4:
            act[car] += "-"
            if winner_score < len(act[car]):
                winner_score = len(act[car])
        print(car," : ", act[car])
    print()

str_output = "최종 우승자: "
for key, value in act.items():
    if len(value) == winner_score:
        str_output += key + ", "

print(str_output[:-2])