n = int(input())
price = list(map(int, input().split()))

arr_profit=[0]


for i in range(len(price)-1):
    for q in range(i,len(price),1):
        if price[q]-price[i]>0:
            arr_profit.append(price[q]-price[i])

print(max(arr_profit))