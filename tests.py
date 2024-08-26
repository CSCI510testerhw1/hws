import pytest
from hw1 import factorial


#factorial of 0 test, this test case passes
def test_factorial_zero():
    assert factorial(0)==1, "Factorial of 0 must return 1"

#factorial of 3 ttest, this fails as factorial of 3 is 6 and not 1
def test_factorial_zero():
    assert factorial(3)==1, "Factorial of 3 must return 1"