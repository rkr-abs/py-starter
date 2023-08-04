def add(first_operand, second_operand):
    return first_operand + second_operand

def subtract(first_operand, second_operand):
    return first_operand - second_operand

def multiply(first_operand, second_operand):
    return first_operand * second_operand

def divide(first_operand, second_operand):
    if second_operand == 0:
        return "Error: Cannot divide by zero!"
    return first_operand / second_operand

def calculator(data):
		[operator,first_operand,second_operand] = data
		operations = {"add":add,"sub":subtract,"mul":multiply,"div":divide}

		return operations[operator](float(first_operand),float(second_operand))
