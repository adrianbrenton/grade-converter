from app.model.csv_converter import *


def test_percent_to_float():
    assert percent_to_float(" 29.8 % ") == 29.8
    assert percent_to_float(54.6) == 54.6


def test_converted_score():
    assert converted_score(29) == 29

