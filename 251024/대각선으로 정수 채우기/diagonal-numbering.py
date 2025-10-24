n, m = list(map(int, input().split()))

# Please write your code here.

arr=[
    [0 for _ in range(m)]
    for _ in range(n)
]

num=1

count=0

while True:
    x=count
    y=0
    while True:
        if x>=0 and x<m and y<n:
            arr[y][x]=num
            num+=1
            x-=1
            y+=1
        elif x>=m:
            x-=1
            y+=1
        else:
            break
    if num>(n*m):
        break
    count+=1

for i in range(n):
    for q in range(m):
        print(arr[i][q],end=" ")
    print()



        


