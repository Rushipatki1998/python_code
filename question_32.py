# Q32.write a python program to find count of same element in two lists


list1=[1,2,3,45,45,5,45,45,4]
list2=[1,2,34,5,6,7,8,9]
list3=list(filter(lambda x:x in list1,list2))
print(list3)
