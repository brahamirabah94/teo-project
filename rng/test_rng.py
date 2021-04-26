import rng
import socket
import pytest

hostname = socket.gethostname()

@pytest.fixture 
def tester():
    tester = rng.index()
    return tester

def test_index_type(tester):
    assert type(tester) is str

def test_index_content(tester):
    assert  "RNG running on {}\n".format(hostname) in tester 

@pytest.fixture 
def test():
    test = rng.rng(32)
    return test

def test_rng_status(test):
    statuscode = test.status_code
    assert statuscode == 200

def test_rng_content(test):
    content = test.content_type
    assert content == "application/octet-stream"
