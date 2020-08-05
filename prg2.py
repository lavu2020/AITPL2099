#program to find traingle of numbers
rows=5
for row in range(1,rows):
   for column in range(row,0,-1):
        print(column,end=' ')
    print(" ")
#program to find second and fourth largest number
L=[10,20,30,40]
l=list(map(int(input().split())))
l.sort()
print(l)
print("2nd large number is {0},4th large number{1}".format(l[-2],[-4]))
#program third and fifth largest number
l=list(map(int(input().split())))
l.sort()
print(l)
print("2nd large number is {0},4th large number{1}".format(l[-3],[-5]))
