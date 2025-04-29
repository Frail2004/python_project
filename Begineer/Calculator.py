print( "\n<--Calculator-->\n")

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")


choice = int(input("enter your choice in range(1,5): "))
if choice in [1,2,3,4]:
    
    a = int(input("enter first number:"))
    b= int(input("enter second number for calculations: "))


if choice == 1:
    print(f"the sum is {a+b}")

elif choice ==2:
    print(f"the difference is {a-b}")

elif choice==3:
    print(f"the product is {a*b}")

elif choice==4:
    if b ==0:
        print("cannot divided by zero")
    else:
        print(f"the division is {a/b}")

else:
    print("invalid choices")
