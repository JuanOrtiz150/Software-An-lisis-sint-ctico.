import ply.yacc as yacc
from calculadoraLex import tokens

# Reglas de precedencia
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
)

# Gramática


def p_statement_expr(p):
    'statement : expression'
    print("Resultado:", p[1])


def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        try:
            p[0] = p[1] / p[3]
        except ZeroDivisionError:
            print("Error: División entre cero")
            p[0] = 0


def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]


def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]


def p_error(p):
    print("Error de sintaxis", p)


parser = yacc.yacc()
