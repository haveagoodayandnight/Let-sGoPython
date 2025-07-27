x=int(input())
p=1
count=0
arr=list()
while True:
    arr.append(x*p)
    if (x*p)%5==0:
        count+=1
    if count==2:
        break
    p+=1
    

for elem in arr:
    print(elem,end=" ")

    