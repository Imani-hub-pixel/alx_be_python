First_number=int(input("Enter the first number:"))
second_number=int(input("Enter the second number:"))
operation=input("Choose the operation(+,-,*,/:").strip()
match operation:
    case "+":
        result=First_number+second_number
    case "-":
        result=First_number-second_number
    case "*":
        result=First_number*second_number  
    case "/":
        if second_number!=0:
            result=First_number/second_number
        else:
            print("Cannot divide by zero")
print("The result is ",result)
