# Q23.write the program to listify the given list individually

list1 = ["rushi", "patki", "boss"]
list2 = list(map(lambda x: list(x), list1))
print(list2)
