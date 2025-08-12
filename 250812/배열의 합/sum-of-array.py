arr1=list()

for i in range(4):
    arr2=list(map(int,input().split()))
    arr1.append(arr2)


for i in range(4):
    print(sum(arr1[i]))