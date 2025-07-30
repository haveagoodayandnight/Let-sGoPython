arr=list(map(int,input().split()))

N_1=arr[0]
N_2=arr[1]

arr_A=arr=list(map(int,input().split()))
arr_B=arr=list(map(int,input().split()))

arr_whereisit=list()

cnt=0

for i in range(len(arr_A)):
    if arr_A[i]==arr_B[0]:
        arr_whereisit.append(i)
if arr_B[0] in arr_A:
    for arrelem in arr_whereisit:
        if len(arr_B)>(len(arr_A)-arrelem):
            continue
        else:
            para=0
            for i,elem in enumerate(arr_B):          
                if arr_A[i+arrelem]==elem:
                    continue
                else:
                    para+=1
                    break
            if para==1:
                continue
            else:
                cnt+=1


if cnt>=1:
    print("Yes")
else:
    print("No")