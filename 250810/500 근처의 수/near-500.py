arr=list(map(int,input().split()))

minmax=0
maxmax=1000

for elem in arr:
    if elem>500 and maxmax>elem:
        maxmax=elem
    if elem<500 and minmax<elem:
        minmax=elem

print(minmax,maxmax)
        
    