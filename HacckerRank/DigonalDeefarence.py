"""
1 2 3
4 5 6
7 8 9

have to find (9+5+1)-(3+5+7)

"""

arr= ( [ 2, 5, 7 ], [ 4, 7, 9 ], [10,11,12])

l=0
r=0
n=len(arr)
for i in range(n):
    l=l+arr[i][i]
    r=r+arr[i][n-1-i]
print(abs(l-r))


