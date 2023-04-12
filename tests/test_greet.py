from unittest.mock import patch

import pytest

import src.greet as greet


def fake_greeting_reader():
    return 'Hello'


def test_greet():
    assert greet.greet('Alice', fake_greeting_reader) == 'Hello, Alice.'


@pytest.mark.parametrize('names, expected', [([], []),
                                             (['Alice'], ['Hello, Alice.']),
                                             (['Bob', 'Charlie'], ['Hello, Bob.', 'Hello, Charlie.']),
                                             ])
def test_greet_list(names, expected):
    assert greet.greet_list(names, fake_greeting_reader) == expected


@pytest.mark.parametrize('hour, expected', [(6, 'Good morning'),
                                            (15, 'Good afternoon'),
                                            (21, 'Good evening'),
                                            ])
def test_read_greeting(hour, expected):
    with patch('src.greet.datetime') as mock_datetime:
        mock_datetime.now.return_value.hour = hour
        assert greet.read_greeting() == expected
