N,M=map(int,input().split())


arr=[
    [0 for _ in range(M)]
    for _ in range(N)
]

para=1

for i in range(N):
    for q in range(M):
        arr[i][q]+=para
        para+=1

for row in arr:
    for elem in row:
        print(elem,end=" ")
    print()