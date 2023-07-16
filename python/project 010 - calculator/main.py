from ascii import calculator


def calc(a, b, value):
    if value == "*":
        return a*b
    elif value == "/":
        return a/b
    elif value == "+":
        return a+b
    else:
        return a-b


user = "yes"
counter = 0
print(calculator)


while user == "yes":
    if counter == 0:
        firstValue = float(input('What is the first number?: '))
    else:
        firstValue = response
    secondValue = float(input('What is the second number?: '))

    print("""
        +
        -
        *
        /
        """)
    value = input('pick an operation: ')
    response = calc(firstValue, secondValue, value)
    print(f'The value is {response}')
    user = input('Do you want to continue? yes/no: ').lower()
    counter+=1
print(f'The final value is {response}')