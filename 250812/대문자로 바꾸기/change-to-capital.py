rowarr=list()

for i in range(5):
    columnarr=list(map(str,input().split()))
    for q in range(len(columnarr)):
        columnarr[q]=columnarr[q].upper()
    rowarr.append(columnarr)

for i in range(5):
    for q in range(3):
        print(rowarr[i][q],end=" ")
    print()


