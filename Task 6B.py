#program to print the multiplication table of 9
num=9
for i in range(1,11):
    print (num,'x',i,'=',num*i)

#Check if a program is negative or positive
print("Check if a value is negative or positive")
n=int(input ("Enter The Value:"))
if(n>0):
  print("Number is positive.")
else:
  print("Number is negative.")

# Program to convert the number of days to ages
print("converting the number of days to Years")
Days = int(input ("Enter Days:"))
Years = int(Days/365)
print("Days to Years:", Years)
