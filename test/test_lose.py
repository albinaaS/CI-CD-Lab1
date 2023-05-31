from lab.lab_1 import lose, is_win, win_mes, say_hello

import pytest
import sys
from unittest.mock import patch


def choise():
    return input()

@patch('builtins.input', return_value='1')
def test_choise(mock_input):
    assert choise() == '1'
    assert mock_input.called