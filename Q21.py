# Q21.write a python programme count of occurances of element

str1 = input("enter the string-:  ")
result = list(map(lambda i: str1.count(i), str1))
print(dict(zip(str1, result)))
