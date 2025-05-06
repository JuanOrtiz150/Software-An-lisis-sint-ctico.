from calculadoraLex import lexer
from calculadoraParser import parser


def main():
    while True:
        try:
            s = input('expr > ')
        except EOFError:
            break
        if not s:
            continue
        parser.parse(s)


if __name__ == '__main__':
    main()
