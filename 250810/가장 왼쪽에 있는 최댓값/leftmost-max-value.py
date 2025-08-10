
n = int(input())
a = list(map(int, input().split()))


maxindex=len(a)-1

arr_maxindex=list()


while True:
    maxarr=0
    for i in range(maxindex):
        if maxarr<a[i]:
            maxarr=a[i]
    arr_maxindex.append(a.index(maxarr)+1)
    maxindex=a.index(maxarr)
    if maxindex==0:
        break
   

for elem in arr_maxindex:
    print(elem,end=" ")
    
# Please write your code here.
