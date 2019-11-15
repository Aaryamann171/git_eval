print("This is the main file")
import addition
import Division
import multiplication
import subtraction
import modulus

op = input("Select operation you wish to perform:\n 1.Addtion\n 2.Subraction\n 3. Multiplication\n 4. Division\n 5.Modulus\n")
a = input("Enter the first number: ")
b = input("Enter the second number: ")
if(op==1):
    print(addition.add(a,b))
elif(op==2):
    print(subtraction.sub(a,b))
elif(op==3):
    print(multiplication.multiply(a,b))
elif(op==4):
    print(Division.div(a,b))
elif(op==5):
    print(modulus.mod(a,b))

