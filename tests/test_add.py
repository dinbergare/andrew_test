import pytest

from andrew_test.main import add


@pytest.mark.parametrize(
    "a,b,result",
    [
        (0, 0, 0),
        (1, 1, 2),
        (3, 2, 5),
    ],
)
def test_add(a: int, b: int, result: int):
    assert add(a, b) == result


def test_fail():
    assert 1 == 1
