n=input()
arr=list(map(int,input().split()))


HI=101

for i in range(len(arr)-1):
    xmin=min(arr)
    del arr[arr.index(min(arr))]
    if HI>min(arr)-xmin:
        HI=min(arr)-xmin

print(HI)