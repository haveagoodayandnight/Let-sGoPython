arr1=[
    list(map(int,input().split()))
    for _ in range(3)
]

input()

arr2=[
    list(map(int,input().split()))
     for _ in range(3)
]



for i in range(3):
    for q in range(3):
        print(arr1[i][q]*arr2[i][q],end=" ")
    print()
