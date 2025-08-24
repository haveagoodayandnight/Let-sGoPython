arr1=list()
arr2=list()



for i in range(3):
    arr_para=list(map(int,input().split()))
    arr1.append(arr_para)
input()
for i in range(3):
    arr_para=list(map(int,input().split()))
    arr2.append(arr_para)

for i in range(3):
    for q in range(3):
        print(arr1[i][q]*arr2[i][q],end=" ")
    print()
