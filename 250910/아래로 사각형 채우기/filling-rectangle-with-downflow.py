N=int(input())

arr=[
    [0 for _ in range(N)]
    for _ in range(N)
]

num=1

for i in range(N):
    for q in range(N):
        arr[q][i]=num
        num+=1

for i in range(N):
    for elem in arr[i]:
        print(elem,end=" ")
    print()

