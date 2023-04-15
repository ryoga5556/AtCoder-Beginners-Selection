N,a,b = map(int,input().split())

cnt = 0
for n in range(1,N+1):
    sum = 0
    for digit in list(str(n)):
        sum += int(digit)
    if a <= sum <= b:
        cnt += n
print(cnt)