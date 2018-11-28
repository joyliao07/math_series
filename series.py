fib = [0, 1]
# THIS IS THE FABONACCI SERIES:
# 0, 1, 1, 2, 3, 5, 8, ETC.



def fibonacci(n):
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
    pass




def sum_series():
    #DOC: USING THE SAME LOGICS AS FIBONACCI AND LUCAS, A FUNCTION THAT RETURNS THE nth VALUE OF THE SUM_SERIES
    pass


def test():
    return True



if __name__ == "__main__":
    # fibonacci(6)
    pass






