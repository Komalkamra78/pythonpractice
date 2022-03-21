num=int( input("enter number:"))
factorial=1

for i in range(1,num+1):
    factorial=factorial*i
print(f" the factorial of a given number is:{factorial} ")

# using recursion:

def fact(num):
    if num==0 or num==1:
        return 1
    else:
        return num * fact(num-1)

num=int(input("enter number: "))
factorial= fact(num)
print(f"factorial is {factorial}")
    