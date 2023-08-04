from calculator import calculator

def repl():
    print("Simple Calculator")
    print("Type 'exit' to quit")
    print("Enter an expression (e.g., add 5 3): ")

    while True:
        user_input = input(">> ")

        if user_input.lower() == 'exit':
            break

        splitted_input = user_input.split()

        print("Result:", calculator(splitted_input))


if __name__ == "__main__":
    repl()
