arr_c=list()

for i in range(4):
    arr_r=list(map(int,input().split()))
    arr_c.append(arr_r)

sum=0

for i in range(4):
    for q in range(i+1):
        sum+=arr_c[i][q]

print(sum)