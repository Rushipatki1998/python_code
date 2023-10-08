
    # Q19: Write a python program to remove element in list which is present in other list

    list1 = [4, 56, 7, 75, 5, 34, 3, 536, 54, 676, 87, 98]
    list2 = [54, 676, 87, 98, 98, 43, 43, 43]
    list3 = list(filter(lambda x: x not in list1, list2))
    print(list3)
    # Output: [43, 43, 43]
    