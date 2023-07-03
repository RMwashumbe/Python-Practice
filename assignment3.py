#create a calculator using else and if statements with input output
def add(p,q):
    return p+q
def subtract(p,q):
    return p-q
def multiply (p,q):
    return p*q
def divide (p,q):
    return p/q

print("Select Operation:")
print("a. Addition")
print("b. Subtraction")
print("c. Multiplication")
print("d. Division")

choice = input("Enter choice (a/b/c/d)")
num1=int and float(input("Please enter first number"))
num2=int and float(input("Please enter second number"))

if choice == 'a':
    print(num1,"+",num2,"=",add(num1,num2))
elif choice == 'b':
    print(num1,"-",num2, "=", subtract(num1,num2))
elif choice == 'c':
    print(num1, "*", num2, "=", multiply(num1, num2))
elif choice == 'd':
    print(num1, "/", num2, "=", divide (num1,num2))
else:
    print("Invalid input")