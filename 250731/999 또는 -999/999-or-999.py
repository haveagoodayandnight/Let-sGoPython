arr=list(map(int,input().split()))

minval_arr=arr[0]
maxval_arr=arr[0]

for i in range(len(arr)-2):
    if minval_arr>arr[i+1]:
        minval_arr=arr[i+1]
    if maxval_arr<arr[i+1]:
        maxval_arr=arr[i+1]


print(maxval_arr,minval_arr)