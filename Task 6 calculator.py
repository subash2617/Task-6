a=int(input("Enter a value:"))
choice = input("Enter +,-,* or /: ")
b=int(input("Enter b value:"))
if choice == "+":
    print(a+b)
elif choice == "-":
    print(a-b)
elif choice == "*":
    print(a*b)
elif choice == "/":
    print(a/b)
else:
    print("Invalid Input")