

def test_assert_true():
    assert True is True

def test_series_file():
    from .series import test
    assert test

def test_fibonacci():
    from .series import fibonacci
    input = 4
    expected = 2
    assert fibonacci(input) == expected













