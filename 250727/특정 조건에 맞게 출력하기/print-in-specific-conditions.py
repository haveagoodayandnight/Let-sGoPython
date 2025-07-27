arr= list(map(int,input().split()))

count=0

for elem in arr:
    if elem==0:
        break
    else:
        count+=1

printarr=list()

for elem in arr[:count:1]:
    if elem%2==0:
        elem/=2
    else:
        elem+=3
    printarr.append(int(elem))

for elem in printarr:
    print(elem,end=" ")