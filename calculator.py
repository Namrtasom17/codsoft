def add(a, b):
    
    return a + b

def subtract(a, b):
   
    return a - b

def multiply(a, b):
   
    return a * b

def divide(a, b):
   
    if b == 0:
        return
    return a / b

def display_menu():
   
    print("Select you choice")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

def main():
   
    while True:
        display_menu()
        choice = input("Enter the number")

        if choice in ['1', '2', '3', '4']:
           
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        

            if choice == '1':
                print(add(num1, num2))
            elif choice == '2':
                print(subtract(num1, num2))
            elif choice == '3':
                print(multiply(num1, num2))
            elif choice == '4':
                print(divide(num1, num2))

        elif choice == '5':
            print("You are now exiting this caculator")
            break

        else:
            print("Please select the valid number")

if __name__ == "__main__":
    main()
