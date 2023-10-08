
    # Q12: Write a program to a number which is divisible by 19 or 13

    list1 = eval(input("Enter numbers separated by commas: "))
    print(list1)
    num = list(filter(lambda x: x % 13 == 0 or x % 19 == 0, list1))
    print(num)
    # Example Input: 23, 323, 323, 23, 23, 4, 544, 6, 67, 7
    # Example Output: [323, 323]
    