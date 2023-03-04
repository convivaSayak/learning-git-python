def linear_search(list_numbers, numbers_ToFind):
    for index, element in enumerate(list_numbers):
        if element == numbers_ToFind:
            return index

    return -1


if __name__ == '__main__':
    list_numbers = [12, 13, 14, 15, 16, 17, 18, 19, 20]
    numbers_ToFind = 14

    index = linear_search(list_numbers, numbers_ToFind)

    print(f" number found at index {index} using Linear search")
