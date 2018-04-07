import pytest
from app.model.csv_converter import *


def test_percent_to_float():
    assert percent_to_float(" 29.8 % ")


