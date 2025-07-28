arr=list(map(int,input().split()))

count=0

for elem in arr:
    if elem==0:
        break
    count+=1

count_arr=[0]*10

for elem in arr[:count:1]:
    count_arr[elem//10-1]+=1

for i in range(9):
    print(i+1,'-',count_arr[i])

