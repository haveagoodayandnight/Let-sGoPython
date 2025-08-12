arr1=list()

for i in range(2):
    arr2=list(map(int,input().split()))
    arr1.append(arr2)

for i in range(2):
    print(round((arr1[i][0]+arr1[i][1]+arr1[i][2]+arr1[i][3])/4,1),end=" ")
print()
for i in range(4):
    print(round((arr1[0][i]+arr1[1][i])/2,1),end=" ")
print()
print(round((sum(arr1[1])+sum(arr1[0]))/8,1))
