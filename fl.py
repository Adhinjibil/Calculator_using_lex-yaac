import streamlit as st
import ply.lex as lex
import ply.yacc as yacc
st.title("Calculator using Lex/Yaac")
sel=st.selectbox("select",["About Our Project","Algorithm"])
if sel == 'About Our Project':
    st.info("submitted by Gokul(RA2011030010023) Adhin Jibil(RA2011030010031)")
    st.write('We used PLY library for implementation.PLY is a pure-Python implementation of the popular compiler construction tools lex and yacc.')
if sel=='Algorithm':
    st.write('1.The given aritmetic expression can be converted into Tokens')
    st.image('1.png')
    st.write('2.Using tokens we have to construct syntax  abstract tree')
    st.image('2.png')
    st.write("3.By using syntax tree the result can be calculated")
st.title("calculation")   
data=st.text_input(" ")
tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
)

# Define the regular expressions that will match each token
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'

# Define a regular expression for matching numbers
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Define a regular expression for handling whitespace (ignored by the lexer)
t_ignore = ' \t\n'

# Define a function for handling errors
def t_error(t):
    print(f"Lexer error: unexpected character '{t.value[0]}'")
    t.lexer.skip(1)

# Create the lexer
lexer = lex.lex()
lexer.input(data)

# Tokenize

tok = lexer.token()
st.write('Tokenizing the given arithmetic expression')
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    st.success(tok)

# Define the grammar for the arithmetic expressions
def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = ('+', p[1], p[3])

def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = ('-', p[1], p[3])

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_times(p):
    'term : term TIMES factor'
    p[0] = ('*', p[1], p[3])

def p_term_divide(p):
    'term : term DIVIDE factor'
    p[0] = ('/', p[1], p[3])

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_number(p):
    'factor : NUMBER'
    p[0] = p[1]

def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]

def p_error(p):
    print(f"Syntax error at '{p.value}'")

# Create the parser
parser = yacc.yacc()

# Example arithmetic expression to parse
input_string = data

# Parse the input string and generate the syntax tree
syntax_tree = parser.parse(input_string)

# Print the syntax tree
st.write('Tokens into abstract syntax Tree')
st.success(syntax_tree)
def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = p[1] + p[3]

def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = p[1] - p[3]

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_times(p):
    'term : term TIMES factor'
    p[0] = p[1] * p[3]

def p_term_divide(p):
    'term : term DIVIDE factor'
    p[0] = p[1] / p[3]

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_number(p):
    'factor : NUMBER'
    p[0] = p[1]

def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]

def p_error(p):
    print(f"Syntax error at '{p.value}'")

# Create the parser
parser = yacc.yacc()

# Example arithmetic expression to evaluate
input_string = data

# Parse the input string and evaluate the arithmetic expression
result = parser.parse(input_string)

# Print the result
st.write('Final calculated Result')
st.success(result)

