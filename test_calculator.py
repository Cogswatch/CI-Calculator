import calculator

class TestCalculatorApp:

  def test_add(self):
    assert 4 == calculator.add(2, 2)