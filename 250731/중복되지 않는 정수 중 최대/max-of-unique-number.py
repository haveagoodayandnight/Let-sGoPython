import sys

n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.

cnt=[0]*1001
maxval_nums=-sys.maxsize

for elem in nums:
    cnt[elem]+=1

for i in range(1001):
    if cnt[i]==1:
        if i>maxval_nums:
            maxval_nums=i

if maxval_nums==-sys.maxsize:
    print('-1')
else:
    print(maxval_nums)
        

