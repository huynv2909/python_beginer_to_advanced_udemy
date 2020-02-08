import re

print("Our Magical Calculator")
print("Type 'reset' to reset equation")
print("Type 'quit' to exit")

start = True
run = True
previous = 0
message = "Enter equation:"


def performMath():
    global run
    global previous
    global start
    global message

    input_user = input(message)

    if input_user == 'quit':
        print("Good bye!")
        run = False
    elif input_user == 'reset':
        start = True
        message = "Enter equation:"
    else:
        if start:
            equation = input_user
        else:
            equation = str(previous) + input_user

        start = False
        equation = re.sub('[a-zA-Z,.:()" "]', '', equation)
        previous = eval(equation)

        message = str(previous)


while run:
    performMath()
