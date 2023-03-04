def binary_search(list_numbers,numbers_ToFind):
    lowerBound=0
    uperBound=len(list_numbers)-1
    mid_index=0

    while (uperBound >= lowerBound):
        mid_index = (lowerBound + uperBound )//2
        if list_numbers[mid_index]==numbers_ToFind:
            return mid_index
        if numbers_ToFind > list_numbers[mid_index]:
            lowerBound=mid_index + 1

        else:
            uperBound=mid_index-1

    return -1


if __name__== '__main__':
    list_numbers=[12,13,14,15,16,17,18,19,20]
    numbers_ToFind=14

    index=binary_search(list_numbers,numbers_ToFind)

    print(f" number found at index {index} using binary search")


