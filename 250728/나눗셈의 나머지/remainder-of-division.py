arr_count=[0]*10

arr_input=list(map(int,input().split()))

while True:
    arr_count[arr_input[0]%arr_input[1]]+=1
    arr_input[0]=arr_input[0]//arr_input[1]
    if arr_input[0]==0:
        break

SumOf = 0

for i in range(10):
    if arr_count[i]>0:
        SumOf+=arr_count[i]**2

print(SumOf)