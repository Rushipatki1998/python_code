
    # Q15: Write a program in list where each number is multiplied by a given number using lambda function

    list1 = list(eval(input("Enter numbers separated by commas: ")))
    num = int(input("Enter a number to multiply: "))
    list2 = (lambda x: [i * num for i in list1])
    print(list2(list1))
    # Example Input: 3,23,5,45,46,7,87,799,0 and 10
    # Example Output: [30, 230, 50, 450, 460, 70, 870, 7990, 0]
    