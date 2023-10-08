
# Q3: Write a program to find a square and cube using lambda function
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Our original list is ", list1)

list2 = lambda x: [i*i for i in list1]
list3 = lambda x: [i*i*i for i in list1]

print("Our squares are ", list2(list1))  # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81]  
print("Cubes of list are -:", list3(list1))  # Output: [1, 8, 27, 64, 125, 216, 343, 512, 729]
