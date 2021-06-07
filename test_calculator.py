import calculator


class TestCalculatorApp:

    def test_add(self):
        assert 4 == calculator.add(2, 2)

    def test_sub(self):
        assert 3 == calculator.sub(7, 4)

    def test_mul(self):
        assert 24 == calculator.mul(8, 3)

    def test_div(self):
        assert 3 == calculator.div(24, 8)
