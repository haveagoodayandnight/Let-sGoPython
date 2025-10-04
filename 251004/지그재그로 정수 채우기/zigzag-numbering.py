n, m = list(map(int, input().split()))

# Please write your code here.

arr=[
    [0 for _ in range(m)]
    for _ in range(n)
]

num=0

column=0


while True:
    if column%2 == 0:
        for i in range(n):
            arr[i][column]=num
            num+=1
    else:
        for i in range(n-1,-1,-1):
            arr[i][column]=num
            num+=1
    column+=1
    if n*m==num:
        break

for i in range(n):
    for q in range(m):
        print(arr[i][q],end=" ")
    print()