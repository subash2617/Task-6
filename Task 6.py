# program to loop through a list of numbers and add +2 to every value to elements in list #
List= [1,2,3,4,5]
for x in List:
    print(x+2)

# 2
x = 5
for i in range(0,x+1):
    print()
    for j in range(x-i,0,-1):
        print(j,end='')