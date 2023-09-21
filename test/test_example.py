from aachary3.example import hello
from aachary3.example import add


def test_hello():
    assert hello() == "Hello world v0.1"


def test_add():
    assert add(2, 3) == 5
    assert add(1, 3) == 4
    assert add("hello", " world") == "hello world"
