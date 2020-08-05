#program to find traingle of numbers
rows=5
for row in range(1,rows):
   for column in range(row,0,-1):
       print(column,end=' ')
    print(" ")
#program to find second and fourth largest number
m=int(input("enter number of elements:"))
a=list(map(int,input(" enter the numbers:").strip().split()))
a.sort()
print(a)
print("2nd large number is {0},4th large number{1}".format(a[-2],a[-4]))
#program third and fifth largest number
m=int(input("enter number of elements:"))
a=list(map(int,input(" enter the numbers:").strip().split()))
a.sort()
print(a)
print("3rd large number is {0},5th large number{1}".format(a[-3],a[-5]))
#program third and fifth smallest in th given list
m=int(input("enter number of elements:"))
a=list(map(int,input(" enter the numbers:").strip().split()))
a.sort()
print(a)
print("3rd smallest number is {0},5th smallest number{1}".format(a[3],a[5]))

