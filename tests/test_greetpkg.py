from greetpkg import __version__
from greetpkg.spanish import hola

def test_hola():
    assert hola() == 'hola'


def test_version():
    assert __version__ == '0.1.0'
