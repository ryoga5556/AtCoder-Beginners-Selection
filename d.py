N = int(input())
convert = lambda x: format(int(x),'b')[::-1].find('1')
A = list(map(convert,input().split()))
print(min(A))
