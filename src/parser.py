import re
from src.lexer import TokenType

# ═══════════════════════════════════════════════════════════════
#  AST NODE DEFINITIONS
# ═══════════════════════════════════════════════════════════════

class ASTNode: pass

class ProgramNode(ASTNode):
    def __init__(self): self.statements = []

class InitSovereignLayerNode(ASTNode): pass
class InitViewportNode(ASTNode): pass
class SyncCloudNode(ASTNode): pass
class HaltNode(ASTNode): pass
class ContinueNode(ASTNode): pass

class RenderMatrixNode(ASTNode):
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

class VariableDeclarationNode(ASTNode):
    def __init__(self, name, var_type, value):
        self.name, self.var_type, self.value = name, var_type, value

class StringDeclarationNode(ASTNode):
    """Create a string named X and set it to "value"."""
    def __init__(self, name, value):
        self.name, self.value = name, value

class BoolDeclarationNode(ASTNode):
    """Create a boolean named X and set it to true/false."""
    def __init__(self, name, value):
        self.name, self.value = name, value

class MathOpNode(ASTNode):
    def __init__(self, var_name, operator, amount):
        self.var_name, self.operator, self.amount = var_name, operator, amount

class MathFuncNode(ASTNode):
    """Set X to the sqrt/abs/floor/ceil/power of Y [and Z]."""
    def __init__(self, target, func, operand, operand2=None):
        self.target   = target    # variable to store result
        self.func     = func      # 'sqrt','abs','floor','ceil','pow','max','min','log','exp'
        self.operand  = operand   # primary operand
        self.operand2 = operand2  # secondary (for pow/max/min)

class IncrDecrNode(ASTNode):
    """Increment / Decrement X."""
    def __init__(self, var_name, op):
        self.var_name, self.op = var_name, op  # op = '++' or '--'

class ModuloNode(ASTNode):
    """Find the remainder of X divided by Y and store in Z."""
    def __init__(self, dividend, divisor, target):
        self.dividend, self.divisor, self.target = dividend, divisor, target

class RandomNode(ASTNode):
    """Generate a random number between A and B and store in X."""
    def __init__(self, low, high, target):
        self.low, self.high, self.target = low, high, target

class InputNode(ASTNode):
    """Ask the user to enter a value for X (with optional prompt)."""
    def __init__(self, var_name, prompt=""):
        self.var_name, self.prompt = var_name, prompt

class InputStringNode(ASTNode):
    """Ask the user for text named X (with optional prompt)."""
    def __init__(self, var_name, prompt=""):
        self.var_name, self.prompt = var_name, prompt

class PrintNode(ASTNode):
    def __init__(self, var_name): self.var_name = var_name

class DisplayTextNode(ASTNode):
    """Display "some text" or display multiple variables."""
    def __init__(self, text): self.text = text

class DisplayVarNode(ASTNode):
    """Display the value of X and Y and Z..."""
    def __init__(self, vars_list): self.vars_list = vars_list

class LoopNode(ASTNode):
    def __init__(self): self.body = []

class ForLoopNode(ASTNode):
    """Repeat X times: ..."""
    def __init__(self, count, body):
        self.count, self.body = count, body

class WhileNode(ASTNode):
    """Keep running while X is less than Y: ..."""
    def __init__(self, condition, body):
        self.condition, self.body = condition, body

class IfNode(ASTNode):
    def __init__(self, condition, true_body, false_body):
        self.condition, self.true_body, self.false_body = condition, true_body, false_body

class OverrideBlockNode(ASTNode):
    def __init__(self, code): self.code = code

class CommentNode(ASTNode):
    def __init__(self, text): self.text = text

class PrintLineNode(ASTNode):
    """Print an empty blank separator line."""
    pass

class AssignNode(ASTNode):
    """Set X to Y (direct assignment)."""
    def __init__(self, var_name, value):
        self.var_name, self.value = var_name, value

class SwapNode(ASTNode):
    """Swap the values of X and Y."""
    def __init__(self, a, b): self.a, self.b = a, b

# ═══════════════════════════════════════════════════════════════
#  SELF-HEALING ENGINE
# ═══════════════════════════════════════════════════════════════

class ErrorHealer:
    @staticmethod
    def heal(token):
        R="\033[0m"; Y="\033[93m"; C="\033[96m"; G="\033[90m"; W="\033[97m"; B="\033[1m"
        print(f"\n  {Y}⚠{R}  {B}{W}Self-Healing Engine  ·  Syntax Anomaly Detected{R}")
        print(f"  {G}──────────────────────────────────────────────────────────────────{R}")
        print(f"  {G}Line {token.line:<4}{R}  {Y}{token.value}{R}")
        print(f"\n  {C}Quick Reference:{R}")
        print(f"  {G}·{R}  Variables  : Create a [integer/float] named X and set it to Y.")
        print(f"  {G}·{R}  Strings    : Create a string named X and set it to \"text\".")
        print(f"  {G}·{R}  Boolean    : Create a boolean named X and set it to true.")
        print(f"  {G}·{R}  Input      : Ask the user to enter a value for X.")
        print(f"  {G}·{R}  Input text : Ask the user for text named X.")
        print(f"  {G}·{R}  Math       : Add/Subtract/Multiply/Divide X by Y.")
        print(f"  {G}·{R}  Math funcs : Set X to the sqrt/abs/floor/ceil of Y.")
        print(f"  {G}·{R}  Power      : Raise X to the power of Y.")
        print(f"  {G}·{R}  Random     : Generate a random number between A and B and store in X.")
        print(f"  {G}·{R}  Increment  : Increment X.  /  Decrement X.")
        print(f"  {G}·{R}  Modulo     : Find the remainder of X divided by Y and store in Z.")
        print(f"  {G}·{R}  Assign     : Set X to Y.")
        print(f"  {G}·{R}  Swap       : Swap the values of X and Y.")
        print(f"  {G}·{R}  Display    : Display \"Hello World\".  /  Display the value of X.")
        print(f"  {G}·{R}  Log        : Log the value of X.")
        print(f"  {G}·{R}  Loop       : Begin the main simulation loop.  ...  Halt the simulation.")
        print(f"  {G}·{R}  Repeat     : Repeat 10 times: ... Done.")
        print(f"  {G}·{R}  Condition  : If the X is greater than Y, then: ... Otherwise: ...")
        print(f"  {G}──────────────────────────────────────────────────────────────────{R}\n")

# ═══════════════════════════════════════════════════════════════
#  MULTIVERSE PARSER — Self-Healing AST Engine
# ═══════════════════════════════════════════════════════════════

class MultiverseParser:
    def __init__(self, tokens):
        self.tokens  = tokens
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

    # ── helpers ───────────────────────────────────────────────────────────
    def _peek_contains(self, *keywords):
        v = self.peek().value.lower()
        return any(k in v for k in keywords)

    def _collect_body_until(self, *stop_phrases):
        body = []
        while self.peek().type != TokenType.EOF:
            v = self.peek().value.lower()
            if any(p in v for p in stop_phrases):
                break
            if self.peek().type == TokenType.OVERRIDE_BLOCK:
                break
            stmt = self.parse_statement()
            if stmt:
                body.append(stmt)
        return body

    # ── main dispatcher ───────────────────────────────────────────────────
    def parse_statement(self):
        token   = self.advance()

        if token.type == TokenType.OVERRIDE_BLOCK:
            return OverrideBlockNode(token.value)

        text  = token.value.lower()
        orig  = token.value

        # ── Sovereign / Engine ────────────────────────────────────────────
        if "initialize the cloaked zero-knowledge matrix" in text:
            return InitSovereignLayerNode()
        if "initialize high performance gaming viewport" in text:
            return InitViewportNode()
        if "sync the current game state to google cloud storage" in text:
            return SyncCloudNode()

        # ── Render ────────────────────────────────────────────────────────
        m = re.search(r'render a 3d matrix.*?at coordinates ([\d.-]+),\s*([\d.-]+),\s*([\d.-]+)', text)
        if m:
            return RenderMatrixNode(m.group(1), m.group(2), m.group(3))

        # ── Boolean Declaration ───────────────────────────────────────────
        m = re.search(r'create a boolean named (\w+) and set it to (true|false)', orig, re.IGNORECASE)
        if m:
            val = "1" if m.group(2).lower() == "true" else "0"
            return BoolDeclarationNode(m.group(1), val)

        # ── String Declaration ────────────────────────────────────────────
        m = re.search(r'create a string named (\w+) and set it to ["\']?(.*?)["\']?\s*$', orig, re.IGNORECASE)
        if m:
            return StringDeclarationNode(m.group(1), m.group(2).strip('"\''))

        # ── Numeric Variable Declaration ──────────────────────────────────
        m = re.search(r'create a(?:.*?)(integer|floating point variable) named (\w+) and set it to ([\d.-]+)', orig, re.IGNORECASE)
        if m:
            return VariableDeclarationNode(m.group(2), m.group(1).lower(), m.group(3))

        # ── Direct Assignment ─────────────────────────────────────────────
        m = re.search(r'^set (\w+) to ([\d.\w"\'+-]+)\s*$', orig, re.IGNORECASE)
        if m:
            return AssignNode(m.group(1), m.group(2))

        # ── Swap ─────────────────────────────────────────────────────────
        m = re.search(r'swap the values of (\w+) and (\w+)', orig, re.IGNORECASE)
        if m:
            return SwapNode(m.group(1), m.group(2))

        # ── User Input (numeric) ──────────────────────────────────────────
        m = re.search(r'ask the user to enter a value for (\w+)', orig, re.IGNORECASE)
        if m:
            prompt_m = re.search(r'with prompt ["\'](.+?)["\']', orig, re.IGNORECASE)
            prompt = prompt_m.group(1) if prompt_m else f"Enter value for {m.group(1)}"
            return InputNode(m.group(1), prompt)

        m = re.search(r'ask the user for (?:a )?(?:number|value|integer|float) (?:named |called )?(\w+)', orig, re.IGNORECASE)
        if m:
            return InputNode(m.group(1), f"Enter {m.group(1)}")

        # ── User Input (string/text) ──────────────────────────────────────
        m = re.search(r'ask the user for text (?:named |called )?(\w+)', orig, re.IGNORECASE)
        if m:
            return InputStringNode(m.group(1), f"Enter {m.group(1)}")

        m = re.search(r'ask the user to enter text for (\w+)', orig, re.IGNORECASE)
        if m:
            prompt_m = re.search(r'with prompt ["\'](.+?)["\']', orig, re.IGNORECASE)
            prompt = prompt_m.group(1) if prompt_m else f"Enter text for {m.group(1)}"
            return InputStringNode(m.group(1), prompt)

        # ── Math Functions ────────────────────────────────────────────────
        m = re.search(r'set (\w+) to the square root of ([\w.]+)', orig, re.IGNORECASE)
        if m: return MathFuncNode(m.group(1), 'sqrt', m.group(2))

        m = re.search(r'set (\w+) to the absolute value of ([\w.]+)', orig, re.IGNORECASE)
        if m: return MathFuncNode(m.group(1), 'abs', m.group(2))

        m = re.search(r'set (\w+) to the floor of ([\w.]+)', orig, re.IGNORECASE)
        if m: return MathFuncNode(m.group(1), 'floor', m.group(2))

        m = re.search(r'set (\w+) to the ceiling of ([\w.]+)', orig, re.IGNORECASE)
        if m: return MathFuncNode(m.group(1), 'ceil', m.group(2))

        m = re.search(r'set (\w+) to the natural log of ([\w.]+)', orig, re.IGNORECASE)
        if m: return MathFuncNode(m.group(1), 'log', m.group(2))

        m = re.search(r'set (\w+) to e to the power of ([\w.]+)', orig, re.IGNORECASE)
        if m: return MathFuncNode(m.group(1), 'exp', m.group(2))

        m = re.search(r'set (\w+) to the maximum of ([\w.]+) and ([\w.]+)', orig, re.IGNORECASE)
        if m: return MathFuncNode(m.group(1), 'max', m.group(2), m.group(3))

        m = re.search(r'set (\w+) to the minimum of ([\w.]+) and ([\w.]+)', orig, re.IGNORECASE)
        if m: return MathFuncNode(m.group(1), 'min', m.group(2), m.group(3))

        # Raise X to the power of Y  (sets X = X^Y)
        m = re.search(r'raise (\w+) to the power of ([\w.]+)', orig, re.IGNORECASE)
        if m: return MathFuncNode(m.group(1), 'pow_self', m.group(1), m.group(2))

        # Set X to Y to the power of Z
        m = re.search(r'set (\w+) to ([\w.]+) to the power of ([\w.]+)', orig, re.IGNORECASE)
        if m: return MathFuncNode(m.group(1), 'pow', m.group(2), m.group(3))

        # ── Modulo ────────────────────────────────────────────────────────
        m = re.search(r'find the remainder of (\w+) divided by ([\w.]+) and store in (\w+)', orig, re.IGNORECASE)
        if m: return ModuloNode(m.group(1), m.group(2), m.group(3))

        m = re.search(r'set (\w+) to (\w+) modulo ([\w.]+)', orig, re.IGNORECASE)
        if m: return ModuloNode(m.group(2), m.group(3), m.group(1))

        # ── Random ────────────────────────────────────────────────────────
        m = re.search(r'generate a random (?:number|integer) between ([\w.]+) and ([\w.]+) and store in (\w+)', orig, re.IGNORECASE)
        if m: return RandomNode(m.group(1), m.group(2), m.group(3))

        m = re.search(r'set (\w+) to a random number between ([\w.]+) and ([\w.]+)', orig, re.IGNORECASE)
        if m: return RandomNode(m.group(2), m.group(3), m.group(1))

        # ── Increment / Decrement ─────────────────────────────────────────
        m = re.search(r'increment (\w+)', orig, re.IGNORECASE)
        if m: return IncrDecrNode(m.group(1), '++')

        m = re.search(r'decrement (\w+)', orig, re.IGNORECASE)
        if m: return IncrDecrNode(m.group(1), '--')

        # ── Standard Math Operations ──────────────────────────────────────
        m = re.search(r'add ([\w.]+) to (\w+)', orig, re.IGNORECASE)
        if m: return MathOpNode(m.group(2), '+', m.group(1))

        m = re.search(r'increase (\w+) by ([\w.]+)', orig, re.IGNORECASE)
        if m: return MathOpNode(m.group(1), '+', m.group(2))

        m = re.search(r'subtract ([\w.]+) from (\w+)', orig, re.IGNORECASE)
        if m: return MathOpNode(m.group(2), '-', m.group(1))

        m = re.search(r'decrease (\w+) by ([\w.]+)', orig, re.IGNORECASE)
        if m: return MathOpNode(m.group(1), '-', m.group(2))

        m = re.search(r'multiply (\w+) by ([\w.]+)', orig, re.IGNORECASE)
        if m: return MathOpNode(m.group(1), '*', m.group(2))

        m = re.search(r'divide (\w+) by ([\w.]+)', orig, re.IGNORECASE)
        if m: return MathOpNode(m.group(1), '/', m.group(2))

        # ── Display / Output ──────────────────────────────────────────────
        m = re.search(r'display the values? of (.+)', orig, re.IGNORECASE)
        if m:
            parts = [v.strip() for v in re.split(r'\s+and\s+|\s*,\s*', m.group(1))]
            return DisplayVarNode(parts)

        m = re.search(r'display ["\'](.+?)["\']', orig, re.IGNORECASE)
        if m: return DisplayTextNode(m.group(1))

        m = re.search(r'^display (.+)$', orig, re.IGNORECASE)
        if m:
            inner = m.group(1).strip().strip('"\'')
            return DisplayTextNode(inner)

        m = re.search(r'log the value of (\w+)', orig, re.IGNORECASE)
        if m: return PrintNode(m.group(1))

        m = re.search(r'print a blank line', orig, re.IGNORECASE)
        if m: return PrintLineNode()

        # ── Loops ─────────────────────────────────────────────────────────
        if "begin the main simulation loop" in text:
            loop_node = LoopNode()
            loop_node.body = self._collect_body_until(
                "sync the current game state", "halt the simulation"
            )
            return loop_node

        m = re.search(r'repeat ([\w]+) times?', orig, re.IGNORECASE)
        if m:
            body = self._collect_body_until("done", "end repeat", "sync the current game state")
            if self._peek_contains("done", "end repeat"):
                self.advance()
            return ForLoopNode(m.group(1), body)

        m = re.search(r'keep running while (.+)', orig, re.IGNORECASE)
        if m:
            raw_cond = m.group(1).strip()
            cond = self._build_condition(raw_cond)
            body = self._collect_body_until("stop the loop", "end while", "sync the current game state")
            if self._peek_contains("stop the loop", "end while"):
                self.advance()
            return WhileNode(cond, body)

        # ── Conditionals ──────────────────────────────────────────────────
        full_m = re.search(
            r'if (?:the )?(.*?) (drops below|is less than|is greater than|equals|is not|is) (.+?),? then',
            orig, re.IGNORECASE)
        
        if full_m:
            var1 = full_m.group(1).strip()
            op_raw = full_m.group(2).strip().lower()
            var2 = full_m.group(3).strip()
            
            op_map = {"drops below": "<", "is less than": "<",
                      "is greater than": ">", "equals": "==",
                      "is not": "!=", "is": "=="}
                      
            if var2.lower() == "zero": var2 = "0"
            if var2.lower() == "true": var2 = "1"
            if var2.lower() == "false": var2 = "0"
            
            condition = f"{var1} {op_map.get(op_raw, '==')} {var2}"
            
            true_body = self._collect_body_until("otherwise", "end if", "sync the current game state")
            false_body = []
            
            if self._peek_contains("otherwise"):
                self.advance()
                false_body = self._collect_body_until("end if", "sync the current game state")
                
            if self._peek_contains("end if"):
                self.advance()
                
            return IfNode(condition, true_body, false_body)

        # ── Halt / Continue ───────────────────────────────────────────────
        if "trigger the game over sequence" in text:
            return PrintNode('"GAME OVER SEQUENCE TRIGGERED"')
        if "halt the simulation" in text:
            return HaltNode()
        if "keep the simulation running" in text or text.strip() in ("continue", "otherwise"):
            return ContinueNode()

        # ── Fallthrough ───────────────────────────────────────────────────
        ErrorHealer.heal(token)
        return None

    def _build_condition(self, raw):
        """Convert English condition to C expression."""
        op_map = {
            "is less than": "<", "is greater than": ">",
            "equals": "==", "is not equal to": "!=",
            "is": "==", "drops below": "<",
        }
        for eng, sym in op_map.items():
            m = re.search(rf'(.+?)\s+{re.escape(eng)}\s+(.+)', raw, re.IGNORECASE)
            if m:
                return f"{m.group(1).strip()} {sym} {m.group(2).strip()}"
        return raw  # fallback: pass raw as C expression
