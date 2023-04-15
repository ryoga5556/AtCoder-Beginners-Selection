s = input()[::-1]
tageList = ["dream","dreamer","erase","eraser"]
flag = True
while len(s) > 0:
    flag = True
    for i in range(7,4,-1):
        if s[:i][::-1] in tageList:
            s = s[i:]
            flag = False
    if flag:
        s = ""
if flag:
    print("NO")
else:
    print("YES")

