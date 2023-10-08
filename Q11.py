
    # Q11: Write a programme to add two list using map and lambda

    list1 = [23, 343, 5, 45, 4, 56, 7, 78, 79, 3232]
    list2 = [3, 4, 54, 6, 7, 8, 98, 3, 2, 3232342]
    list3 = list(map(lambda a, b: a + b, list1, list2))
    print(list3)
    # Output: [26, 347, 59, 51, 11, 64, 105, 81, 81, 3235574]
    