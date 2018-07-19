def add (x,y):
    return(x+y)
def division(x,y):
    return(x/y)
def multiplication(x,y):
    return(x*y)
def substraction(x,y):
    return(x-y)

print("select the choice:")
print("1.add")
print("2.division")
print("3.multiplication")
print("4.substraction")

choice=input("enter the choice:")

num1=int(input("enter the number:"))
num2=int(input("enter the number:"))

if choice=='1':
    print(num1,"+", num2,"=", add(num1,num2))
elif choice=='2':
    print(num1,"/",num2,"=", division(num1,num2))
elif choice=='3':
    print(num1,"*",num2,"=", multiplication(num1,num2))
elif choice=='4':
    print(num1,"-",num2,"=", subraction(num1,num2))



