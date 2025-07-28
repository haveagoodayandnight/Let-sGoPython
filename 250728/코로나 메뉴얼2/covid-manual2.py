arr=list()
count_arr=[0]*4

for i in range(3):
    arr=input().split()
    if arr[0]=='Y' and int(arr[1])>=37:
        count_arr[0]+=1
    elif int(arr[1])>=37:
        count_arr[1]+=1
    elif arr[0]=='Y':
        count_arr[2]+=1
    else:
        count_arr[3]+=1

    
for i in range(4):
    print(count_arr[i],end=" ")

if count_arr[0]>=2:
    print('E')




