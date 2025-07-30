length=int(input())

arr = list(map(int,input().split()))

idxcnt=0

cnt=0

while True:
    if cnt>=3:
        break
    else:
        for i in range(arr.index(2)+1):
            del arr[0]
            idxcnt+=1
    cnt+=1

print(idxcnt)