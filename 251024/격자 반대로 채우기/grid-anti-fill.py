N=int(input())

arr=[
    [0 for _ in range(N)]
    for _ in range(N)
]

num=1

r=N-1
c=N-1

para=1

while True:
    if num>N*N:
        break
    if(num%N)==0:
        arr[r][c]=num
        num+=1
        c-=1
        if para==1:
            para=0
        else:
            para=1
    elif para==1:
        arr[r][c]=num
        r-=1
        num+=1
    else:
        arr[r][c]=num
        r+=1
        num+=1

for i in range(N):
    for q in range(N):
        print(arr[i][q],end=" ")
    print()
    