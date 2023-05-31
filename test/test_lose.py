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

def test_win_mes_player():
    assert win_mes(2, 1, "Player") == "WIN of Player 1"
    assert win_mes(2, 3, "Player") == "WIN of Player 2"

@pytest.mark.skip(reason="I just wanna skip it :)")
def test_win_mes_player_skip():
    assert win_mes(3, 3, "Player") == "WIN of Player 1"

@pytest.mark.skipif(sys.version_info > (3,7),reason="python more 3.7")
def test_win_mes_player_skipif():
    assert win_mes(3, 3, "Player") == "WIN of Player 1"

@pytest.mark.parametrize('user_item,bot_item',[
                                                (1,3),
                                                (1,4),
                                                (2,1),
                                                (3,2),
                                                (3,4),
                                                (4,2)
                                            ])
def test_with_mes_player_par(user_item,bot_item):
    assert win_mes(user_item,bot_item,"Player") == "WIN of Player 1"

@pytest.mark.parametrize('user_item,bot_item',[
                                                (1, 1),
                                                (1, 2),
                                                (2, 2),
                                                (2, 3),
                                                (2, 4),
                                                (3, 1),
                                                (3, 3),
                                                (4, 1),
                                                (4, 3),
                                                (4, 4)
                                            ])
def test_with_mes_player_par(user_item,bot_item):
    assert win_mes(user_item,bot_item,"Player") == "WIN of Player 2"


@pytest.mark.parametrize('user_item,bot_item',[
                                                (1,3),
                                                (1,4),
                                                (2,1),
                                                (3,2),
                                                (3,4),
                                                (4,2)
                                            ])
def test_win_mes_win(user_item,bot_item):
    assert win_mes(user_item,bot_item) == "You WIN!"