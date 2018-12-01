"""TO TEST FOR THREE FUNCTIONS IN SERIES.PY."""


def test_fibonacci_valid():
    """TO TEST FIBONACCI WITH A INPUT NUMBER THAT IS VALID."""
    from .series import fibonacci
    input = 4
    expected = 3
    assert fibonacci(input) == expected


def test_fibonacci_too_big():
    """TO TEST FIBONACCI WITH AN INVALID INPUT THAT IS TOO BIG."""
    from .series import fibonacci
    input = 1000
    expected = 'The number is too big. Please enter a number between 0 and 999.'
    assert fibonacci(input) == expected


def test_fibonacci_negative():
    """TO TEST FIBONACCI WITH AN INVALUD INPUT THAT IS NEGATIVE."""
    from .series import fibonacci
    input = -1
    expected = 'The number cannot be negative.'
    assert fibonacci(input) == expected


def test_lucas_valid():
    """TO TEST LUCAS WITH A VALUD INPUT."""
    from .series import lucas
    input = 4
    expected = 7
    assert lucas(input) == expected


def test_lucas_too_big():
    """TO TEST LUCAS WITH AN INVALUD INPUT THAT IS TOO BIG"""
    from .series import lucas
    input = 1000
    expected = 'The number is too big. Please enter a number between 0 and 999.'
    assert lucas(input) == expected


def test_lucas_negative():
    """TO TEST LUCAS WITH AN INVALUD NEGATIVE INPUT."""
    from .series import lucas
    input = -1
    expected = 'The number cannot be negative.'
    assert lucas(input) == expected


def test_sum_series_valid():
    """TO TEST SUM_SERIES WITH A VALID INPUT."""
    from .series import sum_series
    input = 4
    expected = 3
    assert sum_series(input) == expected


def test_sum_series_too_big():
    """TO TEST SUM_SERIES WITH AN INVALID INPUT THAT'S TOO BIG."""
    from .series import sum_series
    input = 1000
    expected = 'The number is too big. Please enter a number between 0 and 999.'
    assert sum_series(input) == expected


def test_sum_series_negative():
    """TO TEST SUM_SERIES WITH AN INVALID NEGATIVE INPUT."""
    from .series import sum_series
    input = -1
    expected = 'The number cannot be negative.'
    assert sum_series(input) == expected


def test_result_with_valid_input(capsys):
    """To test result() to properly answer with a valid input."""
    from .series import result
    user_input = 'fibonacci(5)'
    result(user_input)
    captured = capsys.readouterr()
    assert captured.out == '5\n'


def test_result_exception(capsys):
    """To test result() to properly raise exceptions."""
    from .series import result
    user_input = 'I need a number.'
    result(user_input)
    captured = capsys.readouterr()
    assert captured.out == 'Please enter a valid input. For example, "fibonacci(n)", "lucas(n)", or "sum_series(n)".\n'
