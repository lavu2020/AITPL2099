#python program to check whether the string is palindrome or not
my_string = input("ënter a string:")
if(my_string==my_string[::-1]):
    print("the string is palindrome")
else:
    print("the string is not palindrome")
#find largest of three numbers
num1=10
num2=20
num3=30
if(num1>num2) and (num1>num3):
  largest =num1
elif(num2>num1) and (num2>num3):
    largest=num2
else:
    largest=num3
print("the largest number is:",largest)
#find largest number in the given list
list=[10,20,30,40,50]
list.sort
print("the largest number in given list is:",max(list))
#python program to sort words in alphabetical order
my_str=input("ënter a string")
words=my_str.split()
words.sort()
for word in words:
    print(word)
#check the given number is prime or not
num=int(input("ënter a number:"))
if num > 1:
  for i  in range(2,num):
     if(num % i) == 0:
          print(num,"not a prime number")
          break
      else:
          print(num,"is a prime number")
else:
      print(num,"is not a prime number")
 #find prime number between m and n using for statement
m=int(input("enter the prime range m:"))
n=int(input("enter the prime range n:"))
for num in range(m,n + 1):
       if num>1:
           for i in range(2,num):
               if(num%i)==0:
                   break
           else:
              print(num)

