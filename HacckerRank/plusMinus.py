arr=[2,3,-3,5,0,-7,4]
l=len(arr)
plus=minus=zero=0
for i in range(l):
    if arr[i] > 0:
        plus=plus+1
    elif arr[i] <0:
        minus=minus+1
    else:
        zero=zero+1
print(plus/l)