arr = list(map(int,input().split()))

main_arr = list(map(int,input().split()))



for i in range(arr[1]):
    arr_input=list(map(int,input().split()))
    if arr_input[0]==1:
        print(main_arr[arr_input[1]-1])
    elif arr_input[0]==2:
        if arr_input[1] in main_arr:
            print(main_arr.index(arr_input[1])+1)
        else:
            print('0')
    else:
        for elem in main_arr[arr_input[1]-1:arr_input[2]:1]:
            print(elem,end=" ")
        print()