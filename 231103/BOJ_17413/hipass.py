s = input()

s += " "
html = False
normal = False
idx = 0
result = ""
word = False
for i in range(len(s)):
    if s[i] == "<":
        html = True
        idx = i
        continue

    elif s[i] == ">":
        html = False
        result += s[idx:i+1]
        idx = i+1
        continue

    elif s[i] == " ":
        if html:
            continue
        else:
            temp = s[idx:i]
            temp1 = temp[::-1]
            result += (temp1 + " ")
        word = False

    else:
        if word:
            continue
        else:
            idx = i
            word = True

print(result[:-1])
        



