import pytest

from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"


@pytest.fixture
def coll_fixture():
    return [1, 2, 3]


def test_slice(coll_fixture):
    assert arrs.my_slice(coll_fixture, 1, 3) == [2, 3]


def test_slice_a(coll_fixture):
    assert arrs.my_slice(coll_fixture, 1) == [2, 3]


def test_slice_b(coll_fixture):
    assert arrs.my_slice(coll_fixture) == [1, 2, 3]


def test_slice_c(coll_fixture):
    assert arrs.my_slice([]) == []
