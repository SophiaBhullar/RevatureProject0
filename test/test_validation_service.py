from service.validation_service import *
import pytest

@pytest.mark.parametrize("test_name, expected", (
    ("A", False), (" ", False), (".....",False),("Sophia", True),("Tom", True),("gusgwdgiwgdgugffugfygfu", False),
    ("         egfcuyqgdwywgujgu", False),("44625", False),("dadfsf ffff",False)
))
def test_validate_first_name(test_name, expected):
    assert validate_first_name(test_name) == expected


@pytest.mark.parametrize("test_name, expected", (
    ("A", False), (" ", False), (".....",False),("Sophia", True),("Tom", True),("gusgwdgiwgdgugffugfygfu", False),
    ("         egfcuyqgdwywgujgu", False),("44625", False),("dadfsf ffff",False)
))
def test_validate_last_name(test_name, expected):
    assert validate_last_name(test_name) == expected


@pytest.mark.parametrize("test_name, expected", (
    ("A", False), (" ", False), (".....",False),("Sophia", True),("Tom", True),("gusgwdgiwgdgugffugfygfu", False),
    ("         egfcuyqgdwywgujgu", False),("44625", False),("dadfsf ffff",False)
))
def test_validate_username(test_name, expected):
    assert validate_username(test_name) == expected



@pytest.mark.parametrize("test_name, expected", (
    ("Sophiaa", True),
    ("123", False)
))
def test_validate_pasword(test_name, expected):
    assert validate_password(test_name) == expected




