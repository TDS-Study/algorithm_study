'''
생산공정
'''
# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

user_input = int(input())

process = []
for i in range(user_input):
    process.append(input())

faulty = int(input())
spels = []
for i in range(faulty):
    spels.append(input())

for spel in spels:
    answer = {}
    for p in process:
        if p[:len(spel)] == spel:
            if p in answer:
                answer[p] += 1
            else:
                answer[p] = 1
    
    if len(answer.keys()) < 1:
        print(0)
    else:
        max_v = max(answer.values())
        answer_k = []
        for k,v in answer.items():
            if max_v == v:
                answer_k.append(k)
        
        answer_k.sort()
        print(answer_k[0]+ " "+ str(max_v))
    
    
# print ("Hello Goorm! Your input is " + user_input)