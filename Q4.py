
# Q4: Write a program to check whether string starts with a given character
str1 = input("Enter the string-:  ")
char = input("Char-: ")

list2 = lambda x: x.startswith(char)
print(list2(str1))  # Output: True/False based on input
