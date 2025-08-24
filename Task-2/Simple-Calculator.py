print("Simple Calculator") 

while True:
    print("\nNew Calculation:")

    # Take inputs
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("\nChoose operation:")
    print(" +  Addition")
    print(" -  Subtraction")
    print(" *  Multiplication")
    print(" /  Division")
    print(" q  Quit")

    choice = input("Enter choice: ")

    if choice == '+':
        print(f"Result: {num1} + {num2} = {num1 + num2}")
    elif choice == '-':
        print(f"Result: {num1} - {num2} = {num1 - num2}")
    elif choice == '*':
        print(f"Result: {num1} * {num2} = {num1 * num2}")
    elif choice == '/':
        if num2 != 0:
            print(f"Result: {num1} / {num2} = {num1 / num2}")
        else:
            print("Error: Division by zero!")
    elif choice == 'q':
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")
      
