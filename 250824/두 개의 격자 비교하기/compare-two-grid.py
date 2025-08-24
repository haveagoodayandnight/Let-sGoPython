col,row=map(int,input().split())

arr1=[
    list(map(int,input().split()))
    for _ in range(col)
]

arr2=[
    list(map(int,input().split()))
    for _ in range(col)
]

arr3=[
    [0 for _ in range(row)]
    for _ in range(col)
]

for i in range(col):
    for q in range(row):
        if arr1[i][q]!=arr2[i][q]:
            arr3[i][q]+=1
        print(arr3[i][q],end=" ")
    print()

