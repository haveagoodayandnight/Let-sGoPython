n = int(input())
arr = list(map(int, input().split()))

maxlist=list()


for i in range(2):
    maxval_arr=arr[0]
    for i in range(len(arr)-1):
        if maxval_arr<arr[i+1]:
            maxval_arr=arr[i+1]

    maxlist.append(maxval_arr)

    del arr[arr.index(maxval_arr)]

for elem in maxlist:
    print(elem,end=" ")



