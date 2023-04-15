N = int(input())
txy = []
for _ in range(N):
    txy.append(list(map(int,input().split())))
t = 0
x = 0
y = 0
result = True
for data in txy:
    dt = data[0] - t
    dx = abs(data[1] - x)
    dy = abs(data[2] - y)
    diff = dx + dy
    if (diff - dt) % 2 == 0 and diff <= dt:
        result = True
        t,x,y = data[0],data[1],data[2]
    else:
        result = False
        break
if result:    
    print("Yes")
else:
    print("No")