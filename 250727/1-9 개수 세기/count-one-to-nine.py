x=input()
arr=list(map(int,input().split()))
countarr=[0]*9

for elem in arr:
    countarr[elem-1]+=1

for elem in countarr:
    print(elem)

    
