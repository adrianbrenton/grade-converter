import pytest

from app.model.csv_converter import *


def test_percent_to_float():
    assert percent_to_float(" 29.8 % ") == 29.8
    assert percent_to_float(54.6) == 54.6


def test_converted_score():
    assert converted_score(29) == pytest.approx(57.08)
    assert converted_score(50.3) == pytest.approx(71.65)


def test_operate_on_line():
    assert operate_on_line(["John", "Doe", "90.6%", "biz", "baz"]) == \
           ["John", "Doe", converted_score(90.6)]

    assert operate_on_line(["Jane", "Jones", "45%", "foo"],
                           adjuster=converted_score) == \
        ["Jane", "Jones", converted_score(45)]

    assert operate_on_line(["Nicole ", "Davis", "90.6%"],
                           adjuster=lambda x: x/2 + 50) == \
        ["Nicole ", "Davis", pytest.approx(95.3)]


