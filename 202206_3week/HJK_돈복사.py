from collections import deque

balance = [30, 30, 30, 30]
transaction = [[1,2,10],[2,3,20],[3,4,5],[3,4,30]]
abnormal = [1]

def trans(a:int, b:int, amount:int):

    idx_a = a-1
    idx_b = b-1

    dict_a = new_bal[idx_a].pop()
    
    if dict_a["amount"] >= amount:
        # 금액을 빼고 도로 스택에 넣는다
        dict_a["amount"] -= amount

        if dict_a["amount"] > 0: 
            new_bal[idx_a].append(dict_a)

        # 넣어 줄 금액을 만든다 
        new_dic = {"user":dict_a["user"],"amount":amount}

        new_bal[idx_b].append(new_dic)
    else:
        dict_a
        

    balance[idx_a] -= amount
    balance[idx_b] += amount

print(balance)

new_bal = []

for idx, val in enumerate(balance):
    st = deque()
    st.append({"user":idx, "amount":val})

    new_bal.append(st)

print(new_bal)

for i in transaction:

    trans(i[0], i[1], i[2])
    print(f"{i[0]} -> {i[1]}, {i[2]}")
    print(balance)

