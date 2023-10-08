# Q31.write apython program to find diff betn two lists using filter function


list1=[776,454,65,76,7,5324]
list2=[5667,65,85,723,4,234]
list3=list(filter(lambda a:a not in list2,list1))
print(list3)

list4=list(filter(lambda a:a not in list1,list2))
print(list4)
num=0
list6=[]
for i in list3:
    a=i-list4[num]
    num=num+1
    list6.append(a)
print(list6)
