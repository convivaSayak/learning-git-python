candels=[4,5,6,7,8,1,8]
maximum=max(candels)
count=0
n =len(candels)
for i in range (n):
    if candels[i]==maximum:
        count=count+1
print(count)
