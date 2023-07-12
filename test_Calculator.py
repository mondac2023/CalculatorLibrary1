import Calculator


class Test_Calculator:
    def test_addition(self):
        assert Calculator.add(2, 2) == 4

    def test_subtraction(self):
        assert Calculator.subtract(4, 3) == 1
