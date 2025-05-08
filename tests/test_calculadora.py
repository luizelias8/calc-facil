import pytest
from calc_facil import Calculadora


class TestCalculadora:
    def setup_method(self):
        self.calc = Calculadora()

    def test_soma(self):
        assert self.calc.soma(2, 3) == 5
        assert self.calc.soma(-1, 1) == 0
        assert self.calc.soma(-1, -1) == -2

    def test_subtracao(self):
        assert self.calc.subtracao(5, 3) == 2
        assert self.calc.subtracao(2, 3) == -1
        assert self.calc.subtracao(-1, -1) == 0

    def test_multiplicacao(self):
        assert self.calc.multiplicacao(2, 3) == 6
        assert self.calc.multiplicacao(-1, 3) == -3
        assert self.calc.multiplicacao(-2, -3) == 6

    def test_divisao(self):
        assert self.calc.divisao(6, 3) == 2
        assert self.calc.divisao(5, 2) == 2.5
        assert self.calc.divisao(-6, 3) == -2

    def test_divisao_por_zero(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.divisao(5, 0)

    def test_potencial(self):
        assert self.calc.potencia(2, 3) == 8
        assert self.calc.potencia(5, 2) == 25
        assert self.calc.potencia(2, 0) == 1
        assert self.calc.potencia(0, 5) == 0
        assert self.calc.potencia(2, -1) == 0.5

    def test_raiz_quadrada(self):
        assert self.calc.raiz_quadrada(4) == 2
        assert self.calc.raiz_quadrada(9) == 3
        assert self.calc.raiz_quadrada(0) == 0
        assert round(self.calc.raiz_quadrada(2), 4) == 1.4142

    def test_raiz_quadrada_numero_negativo(self):
        with pytest.raises(ValueError):
            self.calc.raiz_quadrada(-4)

    def test_juros_compostos(self):
        assert round(self.calc.juros_compostos(1000, 0.05, 2), 2) == 1200.00
