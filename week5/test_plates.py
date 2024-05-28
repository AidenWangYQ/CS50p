from plates import is_valid


# check if plates.py has a length check
def test_length_check():
    assert is_valid("ab1234") == True
    assert is_valid("thisislongerthanexpected") == False

# check if plate.py has alphanumeric characters check
def test_alnum_check():
    assert is_valid("cs50!!") == False

# for correct length, check if 6 alphabetic plate returns true
def test_validity_6():
    assert is_valid("abcdef") == True

# for correct length, check if types of 5 alphabetic plates gives valid response
def test_validity_5():
    assert is_valid("abcde0") == False
    assert is_valid("abcde1") == True

# for correct length, check if types of 4 alphabetic plates gives valid response
def test_validity_4():
    assert is_valid("abcd00") == False
    assert is_valid("abcd10") == True
    assert is_valid("abcd1a") == False

# for correct length, check if types of 3 alphabetic plates gives valid response
def test_validity_3():
    assert is_valid("abc000") == False
    assert is_valid("abc100") == True
    assert is_valid("abc1ab") == False

# for correct length, check if types of 2 alphabetic plates gives valid response
def test_validity_2():
    assert is_valid("ab0000") == False
    assert is_valid("ab1000") == True
    assert is_valid("ab1abc") == False

# for correct length, check if 1 alphabetic plate returns false
def test_validity_1():
    assert is_valid("a10000") == False