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

def test_lose_message():
    assert lose() == "YOU LOSE!"

def test_is_win():
    assert is_win(1, 3) == True
    assert is_win(4, 1) == False

def test_is_win_draw():
    assert is_win(3, 3) == False

def test_win_mes():
    assert win_mes(1, 3) == "You WIN!"
    assert win_mes(5, 4) == "You LOSE!"