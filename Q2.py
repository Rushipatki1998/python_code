
# Q2: Write the program to sort the dictionary using lambda
list1 = [{"age": 20}, {"age": 25}, {"age": 19}]
print("Our original list", list1)

list1.sort(key=lambda x: x["age"])
print("Our sorted list-: ", list1)  # Output: [{'age': 19}, {'age': 20}, {'age': 25}]
