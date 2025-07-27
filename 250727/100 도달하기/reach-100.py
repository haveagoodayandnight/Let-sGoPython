arr=list()
arr.append(1)
arr.append(input())



while True:
    arr.append(int(arr[-1])+int(arr[-2]))
    if arr[-1]>100:
        break

for elem in arr:
    print(elem,end=" ")