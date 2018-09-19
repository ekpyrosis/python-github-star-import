
from github_star_import import longest
from github_star_import.cli import main


def test_main():
    assert main([]) == 0


def test_longest():
    assert longest([b'a', b'bc', b'abc']) == b'abc'
