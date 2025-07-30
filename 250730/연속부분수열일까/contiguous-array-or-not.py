arr=list(map(int,input().split()))

N_1=arr[0]
N_2=arr[1]

arr_A=arr=list(map(int,input().split()))
arr_B=arr=list(map(int,input().split()))

if arr_B[0] in arr_A:
    if len(arr_B)>=(len(arr_A)-arr_A.count(arr_B[0])):
        print("No")
    else:
        para=0
        for i,elem in enumerate(arr_B):
            if i<arr_A.count(arr_B[0]):
                continue
            else:
                if arr_A[i+arr_A.count(arr_B[0])]==elem:
                    continue
                else:
                    para+=1
                    break
        if para==0:
            print("Yes")
        else:
            print("No")
else:
    print("No")