print("Select the operators: ")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplicaion")
print("4. Division")

while True:
        choice = input("Enter choice (1/2/3/4): ")
        if choice in ('1','2','3','4',):
                num1=float(input("Enter the first number: "))
                num2=float(input("Enter the second number: "))

        if choice == '1':
                print(num1, "+", num2, "=", num1 + num2) 

        elif choice == '2':
            print(num1, "-", num2, "=", num1 - num2)

        elif choice == '3':
                print(num1, "*", num2, "=", num1 * num2)

        elif choice == '4':
            if num2 == 0: 
                print("Error!")
            else:         
                print(num1, "/", num2, "=", num1 / num2) 
            break
        else:
              print("Invalid Input")
                                   
                           
                                      


        