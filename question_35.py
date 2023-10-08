# Q35.write apython programme to find non vowel in list


str1=input("enter the string-:  ")
str2=str1.lower()
list1=[]
for i in str2:
    
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
        list1.append(i)
    else:
        list1.append(i)
print(list1)
vow=list(filter(lambda x:x=="a" or x=="e" or x=="i" or x=="o" or x=="u",list1))
space=list(filter(lambda x:x==" ",list1))
list3=list(filter(lambda x:x not in vow,list1))
print(list3)
