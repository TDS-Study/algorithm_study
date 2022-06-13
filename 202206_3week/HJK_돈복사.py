from collections import deque

balance = [100, 1, 1, 1, 1]
transaction = [[1,2,100],[2,3,101],[3,4,102],[4,5,103],[5,1,104]]
abnormal = [1]

def trans(a:int, b:int, amount:int):
    
    idx_a = a-1
    idx_b = b-1

    stack_a = stack_balance[idx_a]
    stack_b = stack_balance[idx_b]
    
    dict_a = stack_a.pop()
    
    if dict_a["amount"] >= amount:
        # print(f"{a} -> {b}, {amount}")

        # 금액을 빼고 도로 스택에 넣는다
        dict_a["amount"] -= amount

        if dict_a["amount"] > 0: 
            stack_a.append(dict_a)

        # 최초 소유자 정보와 함께 넣어 줄 금액을 만든다 
        new_dic = {"user":dict_a["user"],"amount":amount}
        # b 에다가 소유자, 금액을 넣는다
        stack_b.append(new_dic)
    else:
        # 있는 만큼만 b에 더해준다
        new_dic = {"user":dict_a["user"],"amount":dict_a["amount"]}
        stack_b.append(new_dic)

        # 모자란 만큼 재귀호출한다
        trans(a, b, amount - dict_a["amount"])
    
# print(balance)

stack_balance = []

for idx, val in enumerate(balance):
    st = deque()
    st.append({"user":idx+1, "amount":val})
    stack_balance.append(st)

# print(new_bal)

# 트랜잭션 처리
for i in transaction:

    trans(i[0], i[1], i[2])
    
    # print(new_bal)

final_balance = []

for i in stack_balance:
    
    sum = 0
    while(i):
        dic = i.pop()

        if dic["user"] in abnormal:
            pass
        else:
            sum += dic["amount"]
    
    final_balance.append(sum)

print(final_balance)
    
