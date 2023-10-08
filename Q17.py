
    # Q17: Write a program to find the list which having max and min length using lambda function

    list1 = eval(input("Enter lists separated by commas: "))
    length = lambda x: [len(i) for i in x]
    p = min(length(list1))
    min_list = lambda x: [i for i in x if len(i) == p]
    q = max(length(list1))
    max_list = lambda x: [i for i in x if len(i) == q]
    print(min_list(list1))
    print(max_list(list1))
    # Example Input: 854949549,[545465,65,656,56,5],566,56,656,[65,65,6,656,656]
    # Example Output: [566, 56, 656]
    #                [854949549]
    