#python program to check whether string is palindrome
my_string=input("enter the string:")
if(my_string==my_string[::-1]):
    print("the string is palindrome")
else:
    print("stringis not palindrome")
#find largest of three numbers
num1=10
num2=20
num3=30
if(num1>num2) and (num1>num3):
    largest=num1
elif(num2>num1) and (num2>num3):
    largest=num2
else:
    largest=num3
    print("the largest number is",largest)
#find second and fourth largest number
a=input("ënter the elements:")
b=a.split()
print("sorted elements in the list are:",sorted(b))
c=sorted(b)
print("2,4 largest numbers are:",c[2],c[4])
find third and fifth largest number
a=input("enter the elements")
b=a.split()
print("sorted elements in the list are:",sorted(b))
c=sorted(b)
print("3,5 largest numbers are:",c[3],c[5])
#find largest number in the given list
list=[10,20,30,40,50]
list.sort
print("the largest number is:",max(list))