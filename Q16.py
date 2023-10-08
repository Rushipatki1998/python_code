
    # Q16: Write a python program to find positive and negative number in list

    list1 = list(eval(input("Enter numbers separated by commas: ")))
    pos = list(filter(lambda x: x > 0, list1))
    neg = list(filter(lambda x: x < 0, list1))
    print(pos)
    print(neg)
    print(sum(pos))
    print(sum(neg))
    # Example Input: 23,45,67,89,233,453,-232,-555,-123
    # Example Output: [23, 45, 67, 89, 233, 453]
    #                [-232, -555, -123]
    #                910
    #                -910
    