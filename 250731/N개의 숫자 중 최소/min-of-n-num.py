n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
minval_a=a[0]
maxval_a=a[0]

for i in range(len(a)-1):
    if minval_a>a[i+1]:
        minval_a=a[i+1]
    if maxval_a<a[i+1]:
        maxval_a=a[i+1]


print(minval_a,maxval_a)
