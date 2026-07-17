import re
from src.lexer import TokenType

class ASTNode:
    pass

class ProgramNode(ASTNode):
    def __init__(self):
        self.statements = []

class InitSovereignLayerNode(ASTNode):
    pass

class VariableDeclarationNode(ASTNode):
    def __init__(self, name, var_type, value):
        self.name = name
        self.var_type = var_type
        self.value = value

class InitViewportNode(ASTNode):
    pass

class RenderMatrixNode(ASTNode):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

class LoopNode(ASTNode):
    def __init__(self):
        self.body = []

class MathOpNode(ASTNode):
    def __init__(self, var_name, operator, amount):
        self.var_name = var_name
        self.operator = operator
        self.amount = amount

class IfNode(ASTNode):
    def __init__(self, condition, true_body, false_body):
        self.condition = condition
        self.true_body = true_body
        self.false_body = false_body

class PrintNode(ASTNode):
    def __init__(self, var_name):
        self.var_name = var_name

class SyncCloudNode(ASTNode):
    pass

class OverrideBlockNode(ASTNode):
    def __init__(self, code):
        self.code = code

class HaltNode(ASTNode):
    pass

class ContinueNode(ASTNode):
    pass

class ErrorHealer:
    @staticmethod
    def heal(token):
        print("=========================================================")
        print(f"🔥 [SELF-HEALING ENGINE] Syntax Anomaly Detected!")
        print(f"  Line {token.line}: '{token.value}'")
        print("  SUGGESTION: Ensure your sentence closely follows NATCOM standards.")
        print("  - Variable Creation: 'Create a [integer/floating point variable] named X and set it to Y.'")
        print("  - Math: 'Add X to Y', 'Subtract X from Y', 'Multiply X by Y', 'Divide X by Y'")
        print("  - Output: 'Log the value of X.'")
        print("  - Loops: 'Begin the main simulation loop.' ... 'Halt the simulation.'")
        print("=========================================================")

class MultiverseParser:
    """
    Self-Healing AST Parser & Multiverse Validator.
    Converts stream of English tokens into an Abstract Syntax Tree.
    Includes fallback heuristics for natural language ambiguity.
    """
    def __init__(self, tokens):
        self.tokens = tokens
        self.current = 0

    def peek(self):
        if self.current < len(self.tokens):
            return self.tokens[self.current]
        return self.tokens[-1]

    def advance(self):
        token = self.peek()
        self.current += 1
        return token

    def parse(self):
        program = ProgramNode()
        while self.peek().type != TokenType.EOF:
            stmt = self.parse_statement()
            if stmt:
                program.statements.append(stmt)
        return program

    def parse_statement(self):
        token = self.advance()
        
        if token.type == TokenType.OVERRIDE_BLOCK:
            return OverrideBlockNode(token.value)
            
        text = token.value.lower()
        original_text = token.value
        
        # [A] Sovereign Layer Initialization
        if "initialize the cloaked zero-knowledge matrix" in text:
            return InitSovereignLayerNode()
            
        # [B] Variable Declaration
        var_match = re.search(r'create a(?: (.*?))? (integer|floating point variable) named (\w+) and set it to ([\d.-]+)', original_text, re.IGNORECASE)
        if var_match:
            return VariableDeclarationNode(var_match.group(3), var_match.group(2).lower(), var_match.group(4))
            
        # [C] Math Operations (Generalized)
        match = re.search(r'add ([\w.-]+) to (\w+)', original_text, re.IGNORECASE)
        if match: return MathOpNode(match.group(2), '+', match.group(1))
        
        match = re.search(r'increase (\w+) by ([\w.-]+)', original_text, re.IGNORECASE)
        if match: return MathOpNode(match.group(1), '+', match.group(2))

        match = re.search(r'subtract ([\w.-]+) from (\w+)', original_text, re.IGNORECASE)
        if match: return MathOpNode(match.group(2), '-', match.group(1))
            
        match = re.search(r'decrease (\w+) by ([\w.-]+)', original_text, re.IGNORECASE)
        if match: return MathOpNode(match.group(1), '-', match.group(2))
            
        match = re.search(r'multiply (\w+) by ([\w.-]+)', original_text, re.IGNORECASE)
        if match: return MathOpNode(match.group(1), '*', match.group(2))
            
        match = re.search(r'divide (\w+) by ([\w.-]+)', original_text, re.IGNORECASE)
        if match: return MathOpNode(match.group(1), '/', match.group(2))
            
        # Output / Logging
        match = re.search(r'log the value of (\w+)', original_text, re.IGNORECASE)
        if match: return PrintNode(match.group(1))
            
        # [D] Spatial Physics & Graphics Setup
        if "initialize high performance gaming viewport" in text:
            return InitViewportNode()
            
        render_match = re.search(r'render a 3d matrix representing a vehicle at coordinates ([\d.-]+),\s*([\d.-]+),\s*([\d.-]+)', original_text, re.IGNORECASE)
        if render_match:
            return RenderMatrixNode(render_match.group(1), render_match.group(2), render_match.group(3))
            
        # [E] Loops
        if "begin the main simulation loop" in text:
            loop_node = LoopNode()
            while self.peek().type != TokenType.EOF:
                next_token = self.peek()
                if "sync the current game state" in next_token.value.lower() or next_token.type == TokenType.OVERRIDE_BLOCK:
                    break
                stmt = self.parse_statement()
                if stmt:
                    loop_node.body.append(stmt)
            return loop_node
                
        # Conditionals
        cond_match = re.search(r'if (the )?(.*?) (drops below|is less than|is greater than|equals|is) (.*?), then', original_text, re.IGNORECASE)
        if cond_match:
            var1 = cond_match.group(2).strip()
            op_raw = cond_match.group(3).strip().lower()
            var2 = cond_match.group(4).strip()
            
            op_map = {
                "drops below": "<",
                "is less than": "<",
                "is greater than": ">",
                "equals": "==",
                "is": "=="
            }
            
            if var2.lower() == "zero": var2 = "0"
            
            condition = f"{var1} {op_map.get(op_raw, '==')} {var2}"
            
            true_body = []
            false_body = []
            
            while self.peek().type != TokenType.EOF and "otherwise" not in self.peek().value.lower():
                true_stmt = self.parse_statement()
                if true_stmt: true_body.append(true_stmt)
            
            if "otherwise" in self.peek().value.lower():
                self.advance()
                while self.peek().type != TokenType.EOF:
                    peek_val = self.peek().value.lower()
                    if "sync the current game state" in peek_val or self.peek().type == TokenType.OVERRIDE_BLOCK:
                        break
                    false_stmt = self.parse_statement()
                    if false_stmt: false_body.append(false_stmt)
                    
            return IfNode(condition, true_body, false_body)
                
        if "trigger the game over sequence" in text:
            return PrintNode("\"GAME OVER SEQUENCE TRIGGERED\"")
            
        if "halt the simulation" in text:
            return HaltNode()
            
        if "keep the simulation running" in text:
            return ContinueNode()
            
        # [F] Cloud Memory Sync Hook
        if "sync the current game state to google cloud storage" in text:
            return SyncCloudNode()

        # If we reach here, trigger Self-Healing
        ErrorHealer.heal(token)
        return None
