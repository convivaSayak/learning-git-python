def binarySearch_1(arr,target):
    start=0
    end=len(arr)-1
    mid=0
    while end >=start:
        mid=(start + end)//2
        if (arr[mid]==target):
            return mid
        if target > arr[mid]:
            end=mid-1

        else:
            start=mid +1

    return -1;






if __name__== '__main__':
    list_numbers=[20,19,18,17,16,15,14,13,12,11,10]
    numbers_ToFind=14

    index=binarySearch_1(list_numbers,numbers_ToFind)

    print(f" number found at index {index} using binary search")


