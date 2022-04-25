n = int(input())
args = [input() for _ in range(n)]
first_line = args[0]
result = list(first_line)

if n > 1:
    text_len = len(args[1])
    other_lines = args[1:]

    for i in range(0, text_len):        
        for arg in other_lines:
            if first_line[i] != arg[i]:
                result.pop(i)
                result.insert(i,"?")
                break

print("".join(result))
