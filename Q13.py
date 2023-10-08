
    # Q13: Write a program to find palindromes in a given string

    str1 = input("enter the string-:  ")
    list1 = str1.split()
    print(list1)
    list2 = list(filter(lambda x: x == "".join(reversed(x)), list1))
    print(list2)
    # Example Input: 'aB BA ABBA'
    # Example Output: ['ABBA']
    