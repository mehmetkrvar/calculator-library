from banka import calculator
calculator_machine=calculator(a=None,b=None)
print(calculator_machine.a)
print(calculator_machine.b)
calculator_machine.a=int(input("Enter first number: "))
calculator_machine.b=int(input("Enter second number: "))
print("Addition: ",calculator_machine.add())
print("Subtraction: ",calculator_machine.sub())
print("Division: ",calculator_machine.div())
print("Multiplication: ",calculator_machine.mul())
