arr=list(map(int,input().split()))

for i in range(8):
    arr.append(int(arr[-1])+int(2*arr[-2]))

for elem in arr:
    print(elem,end=" ")