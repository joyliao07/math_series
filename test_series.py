
#TESTS FOR FIBONACCI -


def test_fibonacci_valid():
    #THIS IS TO TEST FIBONACCI WITH A INPUT NUMBER THAT IS VALID
    from .series import fibonacci
    input = 4
    expected = 2
    assert fibonacci(input) == expected


def test_fibonacci_too_big():
    #THIS IS TO TEST FIBONACCI WITH A INPUT NUMBER THAT IS TOO BIG AND THEREFORE INVALID
    from .series import fibonacci
    input = 1000
    expected = 'The number is too big.'
    assert fibonacci(input) == expected


def test_fibonacci_not_greater_than_zero():
    #THIS IS TO TEST FIBONACCI WITH A INPUT NUMBER THAT IS NOT GREATER THAN ZERO AND THEREFORE INVALID
    from .series import fibonacci
    input = 0
    expected = 'The number has to be greater than 0.'
    assert fibonacci(input) == expected


#TESTS FOR LUCAS -


def test_lucas_valid():
    #THIS IS TO TEST LUCAS WITH A INPUT NUMBER THAT IS VALID
    from .series import lucas
    input = 4
    expected = 4
    assert lucas(input) == expected


def test_lucas_too_big():
    #THIS IS TO TEST LUCAS WITH A INPUT NUMBER THAT IS TOO BIG AND THEREFORE INVALID
    from .series import lucas
    input = 1000
    expected = 'The number is too big.'
    assert lucas(input) == expected


def test_lucas_not_greater_than_zero():
    #THIS IS TO TEST LUCAS WITH A INPUT NUMBER THAT IS NOT GREATER THAN ZERO AND THEREFORE INVALID
    from .series import lucas
    input = 0
    expected = 'The number has to be greater than 0.'
    assert lucas(input) == expected


#TESTS FOR SUM_SERIES -


def test_sum_series_valid():
    #THIS IS TO TEST SUM_SERIES WITH A INPUT NUMBER THAT IS VALID
    from .series import sum_series
    input = 4
    expected = 2
    assert sum_series(input) == expected


def test_sum_series_too_big():
    #THIS IS TO TEST SUM_SERIES WITH A INPUT NUMBER THAT IS TOO BIG AND THEREFORE INVALID
    from .series import sum_series
    input = 1000
    expected = 'The number is too big.'
    assert sum_series(input) == expected


def test_sum_series_not_greater_than_zero():
    #THIS IS TO TEST SUM_SERIES WITH A INPUT NUMBER THAT IS NOT GREATER THAN ZERO AND THEREFORE INVALID
    from .series import sum_series
    input = 0
    expected = 'The number has to be greater than 0.'
    assert sum_series(input) == expected


