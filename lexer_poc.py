from enum import Enum

class TokenType(Enum):
    OPERATOR = 0
    KEYWORD = 1
    TYPE = 2
    STATMENT_OPERATOR = 3
    DECLARATION = 4

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    @staticmethod
    def check(tokens):
        str_tokens = []
        for token in tokens:
            str_tokens.append(f"({token.type.name}, {token.value})")
        return str_tokens

class Lexer:
    def __init__(self, code):
        self.code = code
        self.operators = ["+", "-", "*", "/", "^", "(", ")"]
        self.keywords = ["if", "else", "elif", "return", "switch", "case", "default", "virtual_ha_meleh"]
        self.types = ["int", "str", "bool", "float"]
        self.statment_operators = ["==", "!=", "<", ">", ">=", "<=", "=", "&&", "||"]
        self.declaration = ["var", "const", "static", "let"]

    def tokenize(self):
        tokens_list = []

        for word in self.code.split(" "):
            if word in self.keywords:
                tokens_list.append(Token(TokenType.KEYWORD, word))
            elif word in self.types or word.isnumeric():
                tokens_list.append(Token(TokenType.TYPE, word))
            elif word in self.statment_operators:
                tokens_list.append(Token(TokenType.STATMENT_OPERATOR, word))
            elif word in self.declaration:
                tokens_list.append(Token(TokenType.DECLARATION, word))
            elif word in self.operators:
                tokens_list.append(Token(TokenType.OPERATOR, word))
            else:
                raise TypeError('Unknown token type:', word)
        
        return tokens_list

if __name__ == "__main__":
    code = "var = ( 4 + 5 ) / 2"
    lexer = Lexer(code)
    tokens = lexer.tokenize()
    str_tokens = Token.check(tokens)
    print("Tokens:", str_tokens)
