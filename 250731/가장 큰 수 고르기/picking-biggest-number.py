arr= list(map(int,input().split()))

maxval_arr=arr[0]

for i in range(len(arr)-1):
    if arr[i]<arr[i+1]:
        maxval_arr=arr[i+1]

print(maxval_arr)