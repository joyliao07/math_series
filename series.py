import sys
status = True

# THIS IS THE FABONACCI SERIES:
# 0, 1, 1, 2, 3, 5, 8, ETC.


def fibonacci(n):
    fib = [0, 1]
    #DOC: A FUNCTION THAT RETURNS THE nth VALUE OF THE FABONACCI SERIES
    if n > 2:
        for what in range(3, n+1):
            fib.append(fib[-1]+fib[-2])
        print(fib[-1])
        return(fib[-1])
    elif n <=2:
        print(fib[n-1])


def lucas(n):
    #DOC: A FUNCTION THAT RETURNS THE nth VALUE OF THE LUCAS NUMBERS
    print('we did lucas')


def sum_series():
    #DOC: USING THE SAME LOGICS AS FIBONACCI AND LUCAS, A FUNCTION THAT RETURNS THE nth VALUE OF THE SUM_SERIES
    pass


def test():
    return True


def question():
    print('Please enter your function and input.')
    user_input = input()
    if user_input == 'quit':
        exit()
    else:
        eval(user_input)


if __name__ == "__main__":
    #THIS IS TO SUMMARIZE WHAT THE PROGRAM DOES
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
    user_input = '' #THIS VARIABLE ASSIGNMENT IS REQUIRED

    while status is True:
        question()








