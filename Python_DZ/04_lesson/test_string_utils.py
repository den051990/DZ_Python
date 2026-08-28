import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    (" abc", "abc"),
    ("   abc abc", "abc abc"),
    (" 123", "123"),
    (" a b c", "a b c"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    (" ", ""),
    ("", ""),
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("skypro", "s", True),
    ("abc", "d", False),
    ("123", "1", True),
])
def test_contains_positive(input_str, symbol, expected ):
    assert string_utils.contains(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("sky pro", " ", True),
    ("abc", "", True),
    ("", "1", False),
])
def test_contains_positive(input_str, symbol, expected ):
    assert string_utils.contains(input_str, symbol) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("skypro", "s", "kypro"),
    ("abc", "ab", "c"),
    ("abc", "d", "abc"),
])
def test_delete_symbol_positive(input_str, symbol, expected ):
    assert string_utils.delete_symbol(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("sky pro", " ", "skypro"),
    ("abc", "", "abc"),
])
def test_delete_symbol_negative(input_str, symbol, expected ):
    assert string_utils.delete_symbol(input_str, symbol) == expected
