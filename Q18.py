
    # Q18: Check a list whether it is sorted or not using lambda function

    list1 = [4, 54, 654, 6, 786, 543, 4, 4, 3]
    print(list1)
    list2 = sorted(list1, key=lambda x: x)
    print(list2)
    # Output: [4, 54, 654, 6, 786, 543, 4, 4, 3]
    #         [3, 4, 4, 4, 6, 54, 543, 654, 786]
    