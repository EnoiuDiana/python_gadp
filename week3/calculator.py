def addition(x, y):
    msg = "Operatia a fost realizata cu succes!"
    result = None
    try:
        result = x + y
    except ArithmeticError:
        msg = "Operatia nu a fost realizata cu succes!"
    return result, msg


def subtraction(x, y):
    msg = "Operatia a fost realizata cu succes!"
    result = None
    try:
        result = x - y
    except ArithmeticError:
        msg = "Operatia nu a fost realizata cu succes!"
    return result, msg


def multiplication(x, y):
    msg = "Operatia a fost realizata cu succes!"
    result = None
    try:
        result = x * y
    except ArithmeticError:
        msg = "Operatia nu a fost realizata cu succes!"
    return result, msg


def division(x, y):
    msg = "Operatia a fost realizata cu succes!"
    result = None
    try:
        result = x / y
    except ZeroDivisionError:
        msg = "Nu se poate realiza impartirea la 0!"
    return result, msg


def modulus(x, y):
    msg = "Operatia a fost realizata cu succes!"
    result = None
    try:
        result = x % y
    except ArithmeticError:
        msg = "Operatia nu a fost realizata cu succes!"
    return result, msg


def exponentiation(x, y):
    msg = "Operatia a fost realizata cu succes!"
    result = None
    try:
        result = x ** y
    except ArithmeticError:
        msg = "Operatia nu a fost realizata cu succes!"
    return result, msg


def floor_division(x, y):
    msg = "Operatia a fost realizata cu succes!"
    result = None
    try:
        result = x // y
    except ZeroDivisionError:
        msg = "Nu se poate realiza impartirea la 0!"
    return result, msg


def calculator(x, y, operator):
    result = None
    msg = ''
    if operator == '+':
        result, msg = addition(x, y)
    elif operator == '-':
        result, msg = subtraction(x, y)
    elif operator == '*':
        result, msg = multiplication(x, y)
    elif operator == '/':
        result, msg = division(x, y)
    elif operator == '%':
        result, msg = modulus(x, y)
    elif operator == '**':
        result, msg = exponentiation(x, y)
    elif operator == '//':
        result, msg = floor_division(x, y)
    else:
        msg = "Operatorul introdus nu este corect!"
    return result, msg


def start_app():
    print(
        '''
        Calculator!
        +  > Addition
        -  > Substraction
        *  > Multiplication
        /  > Division
        %  > Modulus
        ** > Exponentiation
        // > Floor Division
        '''
    )
    expr = input("Introduceti operatia dorita (format: x operatie y): ")
    expr = expr.split(' ')
    try:
        x = float(expr[0])
        y = float(expr[2])
        res, msg = calculator(x=float(expr[0]), y=float(expr[2]), operator=expr[1])

        if msg == "Operatia a fost realizata cu succes!":
            if res is not None:
                return f"Rezultatul operatiei {expr[0]} {expr[1]} {expr[2]} este  " + "{:.2f}".format(res) + "!"
        else:
            return msg
    except ValueError:
        return "Numerele introduse sunt eronate!"


print(start_app())
