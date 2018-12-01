"""This module to design fibonacci, lucas and sum_series functions."""
status = True


# 0, 1, 1, 2, 3, 5, 8, ETC.
def fibonacci(n):
    """TO RETURNS THE nth VALUE OF THE FABONACCI SERIES."""
    fib = [0, 1]
    if n < 0:
        print('The number cannot be negative.')
        return('The number cannot be negative.')
    elif n > 999:
        print('The number is too big. Please enter a number between 0 and 999.')
        return('The number is too big. Please enter a number between 0 and 999.')
    elif n < 2:
        print(fib[n])
        return(fib[n])
    elif n >= 2:
        for what in range(2, n+1):
            fib.append(fib[-1]+fib[-2])
        print(fib[-1])
        return(fib[-1])


def lucas(n):
    """TO RETURNS THE nth VALUE OF THE LUCAS NUMBERS."""
    luc = [2, 1]
    if n < 0:
        print('The number cannot be negative.')
        return('The number cannot be negative.')
    elif n > 999:
        print('The number is too big. Please enter a number between 0 and 999.')
        return('The number is too big. Please enter a number between 0 and 999.')
    elif n < 2:
        print(luc[n])
        return(luc[n])
    elif n >= 2:
        for what in range(2, n+1):
            luc.append(luc[-1]+luc[-2])
        print(luc[-1])
        return(luc[-1])


def sum_series(n, a=0, b=1):
    """TO RETURNS THE nth VALUE OF THE SUM_SERIES."""
    # 0, 1, 1, 2, 3, 5, 8, 13, 21
    sum = [a, b]
    if n < 0:
        print('The number cannot be negative.')
        return('The number cannot be negative.')
    elif n > 999:
        print('The number is too big. Please enter a number between 0 and 999.')
        return('The number is too big. Please enter a number between 0 and 999.')
    elif n < 2:
        print(sum[n])
        return(sum[n])
    elif n >= 2:
        for what in range(2, n+1):
            sum.append(sum[-1]+sum[-2])
        print(sum[-1])
        return(sum[-1])


def question():
    """To prompt the question and save user's input."""
    print('Please enter your function and input.')
    user_input = input()
    return user_input


def result(user_input):
    """To output result to the user."""
    if user_input == 'quit':
        exit()
    try:
        eval(user_input)
    except:
        print('Please enter a valid input. For example, "fibonacci(n)", "lucas(n)", or "sum_series(n)".')


if __name__ == "__main__":
    print('''
    This module defines functions that implement mathematical series.

    fibonacci(n):
        Returns the nth value in the fabonacci series.

    lucas(n):
        Returns the nth value in the lucas numbers.

    sum_series(n):
        Returns the nth value in the sum series, with the beginning two numbers in the number series an option for your input.

    To quit the program at any time, enter "quit"
    ''')
    while status is True:
        user_input = question()
        result(user_input)
