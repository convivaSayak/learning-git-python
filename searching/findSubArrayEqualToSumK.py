# arr=[2,3,-4,5,-6,1,9,11,12,13,14,7,8,4,19]
#target= 15
def findSubarrayCount(arr,target):
    count=0
    for i in range(len(arr)):
        summ=0
        for j in range(i,len(arr)):
            summ=summ+arr[j]

            if summ == target:
                count=count+1
    print(count)

arr=[2,3,-4,5,-6,1,9,11,12,13,14,7,8,4,19]
target= 15
findSubarrayCount(arr,target)