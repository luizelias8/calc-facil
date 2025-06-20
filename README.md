# calc-facil

Uma calculadora simples com operações básicas (soma, subtração, multiplicação, divisão, potência e raiz quadrada).

Este projeto foi criado como parte de um treinamento sobre como criar e publicar pacotes Python no PyPI.

## Instalação

```bash
pip install calc-facil
```

## Uso

```python
from calc_facil import Calculadora

# Criar uma instância da calculadora
calc = Calculadora()

# Realizar operações
soma = calc.soma(5, 3) # 8
diferenca = calc.subtracao(5, 3) # 2
produto = calc.multiplicacao(5, 3) # 15
quociente = calc.divisao(6, 3) # 2.0
potencia = calc.potencia(2, 3) # 8
raiz = calc.raiz_quadrada(9) # 3.0

# Tratamento de erros
try:
    resultado = calc.divisao(5, 0)
except ZeroDivisionError as e:
    print(f'Erro: {e}')
```

## Uso via linha de comando (CLI)

Após a instalação, é possível utilizar o comando calc-facil diretamente no terminal:

```bash
calc-facil <operacao> <a> <b>
```

Exemplos:

```bash
calc-facil soma 2 3
# Resultado: 5.0

calc-facil divisao 10 2
# Resultado: 5.0

calc-facil potencia 2 3
# Resultado: 8.0

calc-facil raiz_quadrada 9
# Resultado: 3.0
```

## As operações disponíveis são:

- soma
- subtracao
- multiplicacao
- divisao
- potencia
- raiz_quadrada

## Operações disponíveis

- **soma(a, b)**: Retorna a soma de a e b
- **subtracao(a, b)**: Retorna a diferença entre a e b
- **multiplicacao(a, b)**: Retorna o produto de a e b
- **divisao(a, b)**: Retorna o quociente da divisão de a por b (lança ZeroDivisionError se b for zero)
- **potencia(base, expoente)**: Retorna a base elevada ao expoente
- **raiz_quadrada(numero)**: Retorna a raiz quadrada do número (lança ValueError se o número for negativo)

## Pré-requisitos

- Python 3.6 ou superior

## Licença

Este projeto está licenciado sob a Licença **MIT**. Veja o arquivo [LICENSE](./LICENSE) para mais detalhes.
