import argparse
import sys
from .calculadora import Calculadora


def main():
    """Função principal da interface de linha de comando."""
    parser = argparse.ArgumentParser(
        description='Calculadora simples em Python'
    )
    parser.add_argument(
        'operacao',
        choices=[
            'soma',
            'subtracao',
            'multiplicacao',
            'divisao',
            'potencia',
            'raiz_quadrada',
        ],
        help='Operação a ser realizada',
    )
    parser.add_argument('a', type=float, help='Primeiro número')
    parser.add_argument(
        'b',
        type=float,
        nargs='?',
        help='Segundo número (não necessário para raiz_quadrada)',
    )

    args = parser.parse_args()
    calculadora = Calculadora()

    try:
        if args.operacao == 'soma':
            resultado = calculadora.soma(args.a, args.b)
        elif args.operacao == 'subtracao':
            resultado = calculadora.subtracao(args.a, args.b)
        elif args.operacao == 'multiplicacao':
            resultado = calculadora.multiplicacao(args.a, args.b)
        elif args.operacao == 'divisao':
            resultado = calculadora.divisao(args.a, args.b)
        elif args.operacao == 'potencia':
            resultado = calculadora.potencia(args.a, args.b)
        elif args.operacao == 'raiz_quadrada':
            resultado = calculadora.raiz_quadrada(args.a)

        print(f'Resultado: {resultado}')
        return 0
    except ValueError as e:
        print(f'Erro: {str(e)}', file=sys.stderr)
        return 1
    except Exception as e:
        print(f'Erro inesperado: {str(e)}', file=sys.stderr)
        return 2


if __name__ == '__main__':
    sys.exit(main())
