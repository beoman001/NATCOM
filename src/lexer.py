import re

class TokenType:
    SENTENCE = "SENTENCE"
    OVERRIDE_BLOCK = "OVERRIDE_BLOCK"
    EOF = "EOF"

class Token:
    def __init__(self, type_, value, line):
        self.type = type_
        self.value = value.strip()
        self.line = line

    def __repr__(self):
        return f"<Token {self.type}: {self.value}>"

class SafeFreeFormLexer:
    """
    Safe Free-Form Lexer Engine.
    Parses natural English text and isolates low-level <SYSTEM_OVERRIDE> blocks.
    """
    def __init__(self, source_code):
        self.source_code = source_code
        self.tokens = []
        self.line_num = 1

    def tokenize(self):
        lines = self.source_code.split('\n')
        in_override = False
        override_buffer = []
        
        for line_idx, line in enumerate(lines):
            raw_line = line.strip()
            self.line_num = line_idx + 1

            # Ignore empty lines and standard comments
            if not raw_line or raw_line.startswith('//'):
                continue

            if raw_line == '<SYSTEM_OVERRIDE>':
                in_override = True
                continue
            elif raw_line == '</SYSTEM_OVERRIDE>':
                in_override = False
                self.tokens.append(Token(TokenType.OVERRIDE_BLOCK, '\n'.join(override_buffer), self.line_num))
                override_buffer = []
                continue

            if in_override:
                override_buffer.append(raw_line)
            else:
                sentences = []
                in_quote = False
                quote_char = None
                current = []
                for i, char in enumerate(raw_line):
                    if char in '"\'':
                        if not in_quote:
                            in_quote = True
                            quote_char = char
                        elif quote_char == char:
                            in_quote = False
                    
                    if not in_quote and char in '.!?:' and (i == len(raw_line)-1 or raw_line[i+1].isspace()):
                        sentences.append(''.join(current).strip())
                        current = []
                    else:
                        current.append(char)
                        
                if current:
                    sentences.append(''.join(current).strip())
                    
                for sentence in sentences:
                    if sentence:
                        self.tokens.append(Token(TokenType.SENTENCE, sentence, self.line_num))

        self.tokens.append(Token(TokenType.EOF, "", self.line_num))
        return self.tokens
