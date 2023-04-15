n,y = map(int,input().split())

result = [-1,-1,-1]
for i in range(n+1):
    for j in range(n+1-i):
            if y == 10000 * i + 5000 * j + 1000 * (n-i-j):
                result  = [i,j,n-i-j]
print(*result)                    

