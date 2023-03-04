def binarySearch_2_firstOccurance(arr,target):
    start=0
    end=len(arr)-1
    mid=0
    position_of_first=-1
    while (end >=start):
        mid= (start + end )//2
        if target == arr[mid]:
            position_of_first=mid
            end=mid-1

        if target > arr[mid]:
            start=mid+1

        else:
            end=mid-1

    return position_of_first

# def binarySearch_3_lastOccurance(arr,target):
#     start=0
#     end=len(list_numbers)-1
#     mid=0
#     result=-1
#
#     while (end >= start):
#         mid = (start + end )//2
#         if target==arr[mid]:
#             result=mid
#             start=mid+1
#
#         if target > arr[mid]:
#             start=mid + 1
#
#         else:
#             end=mid-1
#
#     return result


# Function to find the last occurrence of a given number in a sorted list of integers
def findLastOccurrence(nums, target):
    # search space is nums[left…right]
    (left, right) = (0, len(nums) - 1)

    # initialize the result by -1
    result = -1

    # loop till the search space is exhausted
    while left <= right:

        # find the mid-value in the search space and compares it with the target
        mid = (left + right) // 2

        # if the target is located, update the result and
        # search towards the right (higher indices)
        if target == nums[mid]:
            result = mid
            left = mid + 1

        # if the target is less than the middle element, discard the right half
        elif target < nums[mid]:
            right = mid - 1

        # if the target is more than the middle element, discard the left half
        else:
            left = mid + 1

    # return the leftmost index, or -1 if the element is not found
    return result





if __name__== '__main__':
    list_numbers=[5,6,7,8,8,8,8,9,10]
    numbers_ToFind=8

    #index1=binarySearch_2_firstOccurance(list_numbers,numbers_ToFind)
    index2=findLastOccurrence(list_numbers,numbers_ToFind)

    #print(f" number found at first index {index1} using binary search")
    print(f" number found at last index {index2} using binary search")