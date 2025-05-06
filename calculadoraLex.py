import ply.lex as lex

# Lista de tokens
tokens = (
    'NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'LPAREN', 'RPAREN', 'IF', 'ELSE', 'WHILE'
)

# Palabras reservadas
reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE'
}

# Reglas para tokens simples
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'

# Números enteros y decimales


def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t

# Palabras reservadas


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')  # IF, ELSE, WHILE o ID
    return t


# Ignorar espacios y tabulaciones
t_ignore = ' \t'

# Saltar líneas nuevas


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Manejo de errores


def t_error(t):
    print(f"Caracter ilegal '{t.value[0]}'")
    t.lexer.skip(1)


# Construir lexer
lexer = lex.lex()
