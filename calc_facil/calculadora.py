class Calculadora:
    """
    Uma calculadora simples que realiza operações básicas de matemática.
    """

    def soma(self, a, b):
        """
        Soma dois números.

        Args:
            a: Primeiro número
            b: Segundo número

        Returns:
            A soma de a e b
        """
        return a + b

    def subtracao(self, a, b):
        """
        Subtrai b de a.

        Args:
            a: Primeiro número
            b: Segundo número

        Returns:
            A diferença entre a e b
        """
        return a - b

    def multiplicacao(self, a, b):
        """
        Multiplica dois números.

        Args:
            a: Primeiro número
            b: Segundo número

        Returns:
            O produto de a e b
        """
        return a * b

    def divisao(self, a, b):
        """
        Divide a por b.

        Args:
            a: Dividendo
            b: Divisor

        Returns:
            O quociente da divisão de a por b

        Raises:
            ZeroDivisionError: Se b for zero
        """
        if b == 0:
            raise ZeroDivisionError('Não é possível dividir por zero')
        return a / b

    def potencia(self, base, expoente):
        """
        Calcula a potência de um número.

        Args:
            base: Número base
            expoente: Expoente

        Returns:
            O resultado de base elevado ao expoente
        """
        return base**expoente

    def raiz_quadrada(self, numero):
        """
        Calcula a raiz quadrada de um número.

        Args:
            numero: Número para calcular a raiz quadrada

        Returns:
            A raiz quadrada do número

        Raises:
            ValueError: Se o número for negativo
        """
        if numero < 0:
            raise ValueError(
                'Não é possível calcular a raiz quadrada de um número negativo'
            )
        return numero**0.5

    def juros_compostos(self, capital, taxa, tempo):
        """
        Calcula o montante com juros compostos.

        Args:
            capital: Capital inicial
            taxa: Taxa de juros (em decimal, ex: 5% → 0.05)
            tempo: Tempo (número de períodos)

        Returns:
            O montante final após aplicação dos juros
        """
        if taxa > 1:
            taxa = taxa / 100

        return capital * (1 + taxa) ** tempo
