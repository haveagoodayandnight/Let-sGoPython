n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
minval_a=a[0]

cnt=0

for i in range(len(a)-1):
    if minval_a>a[i+1]:
        minval_a=a[i+1]
        cnt=1
    elif minval_a<a[i+1]:
        continue
    else:
        cnt+=1
    


print(minval_a,cnt)
