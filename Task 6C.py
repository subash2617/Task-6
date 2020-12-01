#3.Fibonacci sequence
x=int(input("Enter x value: "))
a=0
b=1
sum=0
count=1
print("Fibonacci Series: ", end = " ")
while(count <= x):
  print(sum, end = " ")
  count += 1
  a = b
  b = sum
  sum = a + b
#4.Armstrong number
num=int(input("\nenter a number: "))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//=10
if num == sum:
    print(num,"is an Armstrong number")
else:
    print(num,"is not an Armstrong number")