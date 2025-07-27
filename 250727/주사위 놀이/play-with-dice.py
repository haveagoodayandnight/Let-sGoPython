arr=list(map(int,input().split()))

countarr=[0]*7

for elem in arr:
    countarr[elem]+=1

for i in range(1,7,1):
    print(i,"-",countarr[i])
