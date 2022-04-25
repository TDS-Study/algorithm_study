n = int(input())
ori_score = [input() for _ in range(n)]
new_score = []
new_avg = 100

if n > 1:
    text_len = len(args[1])
    other_lines = args[1:]

    for i in range(0, text_len):        
        for arg in other_lines:
            if first_line[i] != arg[i]:
                result.pop(i)
                result.insert(i,"?")
                break

print(new_avg)
