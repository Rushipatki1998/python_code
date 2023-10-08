
# Q7: Write a program related to Fibonacci series using lambda
num = int(input("Enter the number-: "))
fab_list = [0, 1]

any(map(lambda _: fab_list.append(sum(fab_list[-2:])), range(2, num)))
print(fab_list[:num])  # Output: Fibonacci series up to 'num'
