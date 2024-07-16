import re

# palavras-chave e operadores para Java
keywords = {
    "abstract", "assert", "boolean", "break", "byte", "case", "catch", "char", "class", "const",
    "continue", "default", "do", "double", "else", "enum", "extends", "final", "finally", "float",
    "for", "goto", "if", "implements", "import", "instanceof", "int", "interface", "long", "native",
    "new", "null", "package", "private", "protected", "public", "return", "short", "static",
    "strictfp", "super", "switch", "synchronized", "this", "throw", "throws", "transient", "try",
    "void", "volatile", "while"
}

# Definição de operadores e suas categorias
operador_aritmetico = {"+", "-", "*", "/", "%", "++", "--", "+=", "-=", "*=", "/=", "%="}
operador_logico = {"&&", "||", "!"}
operador_comparativo = {"==", "!=", "<", ">", "<=", ">="}
operador_atribuicao = {"=", "+=", "-=", "*=", "/=", "%="}
operador_Bit_a_Bit = {"&", "|", "^", "~", "<<", ">>", ">>>", "&=", "|=", "^=", "<<=", ">>=", ">>>="}


# Identificar se um token é uma palavra-chave
def is_keyword(token):
    return token in keywords


# Identificar se um token é um operador aritmético
def is_arithmetic_operator(token):
    return token in operador_aritmetico


# Identificar se um token é um operador lógico
def is_logical_operator(token):
    return token in operador_logico


# Identificar se um token é um operador de comparação
def is_comparison_operator(token):
    return token in operador_comparativo


# Identificar se um token é um operador de atribuição
def is_assignment_operator(token):
    return token in operador_atribuicao


# Identificação dos operadores bit a bit
def is_bitwise_operator(token):
    return token in operador_Bit_a_Bit


# Identificação de Identificadores validos
def is_identifier(token):
    return re.match(r'^[A-Za-z_][A-Za-z0-9_]*$', token) is not None


# Identificação de numeros (Inteiros e flutuantes)
def is_number(token):
    return re.match(r'^\d+(\.\d+)?[fFdD]?$', token) is not None


# Função principal do analisador léxico
def lexical_analyzer(code):
    # Expressão regular para separar tokens
    token_pattern = re.compile(
        r'\d+\.\d*[fFdD]?|\d+|[A-Za-z_][A-Za-z0-9_]*|[+-/*%=]+|==|!=|<=|>=|&&|\|\||!|[{}()\[\];,]|&|\||\^|~|<<|>>|>>>|[+\-*/%=]|<<=|>>=|>>>=|&=|\|=|\^='
    )
    tokens = token_pattern.findall(code)

    # Tabela de símbolos e lista de tokens categorizados
    symbol_table = {}
    token_list = []
    symbol_index = 1

    for token in tokens:
        if is_keyword(token):
            token_list.append(("KEYWORD", token))
        elif is_arithmetic_operator(token):
            token_list.append(("Operador Aritmético", token))
        elif is_logical_operator(token):
            token_list.append(("Operador Lógico", token))
        elif is_comparison_operator(token):
            token_list.append(("Operadores de comparação", token))
        elif is_assignment_operator(token):
            token_list.append(("Operadores Atribuição", token))
        elif is_bitwise_operator(token):
            token_list.append(("Operadores Bit a Bit", token))
        elif is_identifier(token):
            if token not in symbol_table:
                symbol_table[token] = symbol_index
                symbol_index += 1
            token_list.append(("Identificado", symbol_table[token]))
        elif is_number(token):
            token_list.append(("Numero", token))
        else:
            token_list.append(("Separadores", token))

    return token_list, symbol_table


# Função para ler o conteúdo de um arquivo .txt
def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()


# Exemplo de uso
file_path = 'CodigosEmJava/TestCode.txt'
code = read_file(file_path)

tokens, symbol_table = lexical_analyzer(code)

print("Tokens:")
for token in tokens:
    print(token)

print("\nTabela de Símbolos")
for symbol, index in symbol_table.items():
    print(f'| {index} | {symbol} |')
