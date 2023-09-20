from fizzbuzz import fizzbuzz, check_fizz

def test_fizzbuzz_1_is_1():
    assert fizzbuzz(1) == 1

def test_fizzbuzz_41_is_41():
    assert fizzbuzz(41) == 41

def test_fizzbuzz_3_is_fizz():
    assert fizzbuzz(3) == 'fizz'

def test_fizzbuzz_300000000_is_fizz():
    assert check_fizz(3000000003) == True

def test_fizzbuzz_negative_3_is_fizz():
    assert fizzbuzz(-3) == 'fizz'

def test_fizzbuzz_5_is_buzz():
    assert fizzbuzz(5) == 'buzz'

def test_fizzbuzz_20_is_buzz():
    assert fizzbuzz(20) == 'buzz'

def test_fizzbuzz_15_is_fizzbuzz():
    assert fizzbuzz(15) == 'fizzbuzz'

def test_fizzbuzz_0_is_0():
    assert fizzbuzz(0) == 'fizzbuzz'

