def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    result = add(num1, num2)
    print("The result is:", result)
elif choice == '2':
    result = subtract(num1, num2)
    print("The result is:", result)
elif choice == '3':
    result = multiply(num1, num2)
    print("The result is:", result)
elif choice == '4':
    if num2 != 0:
        result = divide(num1, num2)
        print("The result is:", result)
    else:
        print("Error: Cannot divide by zero.")
else:
    print("Invalid choice.")
