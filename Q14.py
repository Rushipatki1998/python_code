
    # Q14: Write a python program to calculate all anagrams in a string

    list1 = list(input("Enter space-separated strings: "))
    str1 = input("enter the string-: ")
    list2 = list(filter(lambda i: "".join(sorted(str1)) == "".join(sorted(i)), list1))
    print(list2)
    # Example Input: 'act cat mat' and 'sat'
    # Example Output: []
    