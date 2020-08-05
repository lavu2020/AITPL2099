def add(x,y):
    return(x+y)
def sub(x,y):
    return(x-y)
def mul(x,y):
    return(x*y)
def div(x,y):
    return(x/y)
def mod(x,y):
    return(x%y)
print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")
print("5.modulus")
choice=int(input("enter your choice:"))
a=int(input("enter first number:"))
b=int(input("enter second number:"))
if choice==1:
    print(a,"+",b,"=",add(a,b))
    print("do you want to continue yes/no:")
elif choice==2:
     print(a,"-",b,"=",sub(a,b))
     print("do you want to continue yes/no:")
elif choice==3:
    print(a,"*",b, "=" ,mul(a,b))
    print("do you want to continue yes/no:")
elif choice==4:
    print(a,"/",b,"=",div(a,b))
    print("do you want to continue yes/no:")
elif choice==5:
    print(a,"%",b,"=",mod(a,b))
    print("do you want to continue yes/no:")
elif choice>5:
    print("invalid choice")



