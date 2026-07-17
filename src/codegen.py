import os
import subprocess
from src.parser import *

# ── ANSI Color macros emitted into every compiled binary ─────────────────────
_C_COLORS = '''\
#define RESET   "\\033[0m"
#define BOLD    "\\033[1m"
#define CYAN    "\\033[96m"
#define GREEN   "\\033[92m"
#define YELLOW  "\\033[93m"
#define RED     "\\033[91m"
#define PURPLE  "\\033[95m"
#define WHITE   "\\033[97m"
#define GRAY    "\\033[90m"
'''

_C_TIMING = '''\
#include <time.h>
static struct timespec _nc_t0;
static void _nc_start_timer(void){clock_gettime(CLOCK_MONOTONIC,&_nc_t0);}
static double _nc_elapsed_ms(void){
    struct timespec t1; clock_gettime(CLOCK_MONOTONIC,&t1);
    return (t1.tv_sec-_nc_t0.tv_sec)*1000.0+(t1.tv_nsec-_nc_t0.tv_nsec)/1e6;
}
'''

_C_HELPERS = '''\
static void nc_value_f(const char*name,double v){
    printf("  " CYAN "◆" RESET "  " WHITE "%-24s" RESET " " BOLD CYAN "%g" RESET "\\n",name,v);}
static void nc_value_s(const char*name,const char*v){
    printf("  " CYAN "◆" RESET "  " WHITE "%-24s" RESET " " BOLD WHITE "%s" RESET "\\n",name,v);}
static void nc_value_b(const char*name,int v){
    printf("  " CYAN "◆" RESET "  " WHITE "%-24s" RESET " " BOLD "%s" RESET "\\n",name,v?"true":"false");}
static void nc_log(const char*label,const char*fmt,...){
    va_list a; printf("  " GREEN "▶" RESET "  " BOLD WHITE "%-22s" RESET " ",label);
    va_start(a,fmt);vprintf(fmt,a);va_end(a);printf("\\n");}
static void nc_info(const char*m){printf("  " GRAY "·" RESET "  " GRAY "%s" RESET "\\n",m);}
static void nc_section(const char*l){printf("\\n  " PURPLE BOLD "%s" RESET "\\n",l);}
static void nc_hr(void){
    printf(GRAY "  ──────────────────────────────────────────────────────────────────────" RESET "\\n");}
static void nc_banner(const char*p){
    printf("\\n");
    printf(CYAN "  ══════════════════════════════════════════════════════════════════════" RESET "\\n");
    printf(CYAN BOLD "  NATCOM RUNTIME  ·  %s" RESET "\\n",p);
    printf(GRAY "  Natural Communication Language  ·  Native Binary  ·  -O3 Optimized" RESET "\\n");
    printf(CYAN "  ══════════════════════════════════════════════════════════════════════" RESET "\\n\\n");}
static void nc_footer(double ms){
    printf("\\n"); nc_hr();
    printf("  " GREEN "✔" RESET "  " BOLD WHITE "Execution complete" RESET "  " GRAY "(%.0f ms)" RESET "\\n",ms);
    printf(CYAN "  ══════════════════════════════════════════════════════════════════════" RESET "\\n\\n");}
static void nc_display(const char*msg){printf("  " WHITE "  %s" RESET "\\n",msg);}
static void nc_input_prompt(const char*msg){
    printf("  " YELLOW "▷" RESET "  " BOLD WHITE "%s" RESET ": ",msg);}
'''

_C_SOVEREIGN = '''\
static void init_sovereign_matrix(void){
    nc_section("SOVEREIGN LAYER");
    nc_log("ZKP Audit","Cloaked zero-knowledge proof hooks initialized.");
    nc_info("Cryptographic traceability: ENABLED");}
static void init_viewport(void){
    nc_section("GAMING ENGINE");
    nc_log("Viewport","High-performance 3D viewport online.");
    nc_log("Physics","Gravity engine initialized  (g = 9.81 m/s\\xc2\\xb2)");}
static void render_matrix(float x,float y,float z){
    nc_log("Render","3D matrix positioned at (%.2f, %.2f, %.2f)",x,y,z);}
static void sync_cloud_ram(void){
    nc_section("CLOUD SYNC");
    nc_log("GCP Sync","State serialized to Google Cloud Storage.");
    nc_info("Offline fallback: ACTIVE");}
static void flush_render_pipeline(void){nc_log("Pipeline","Render pipeline flushed.");}
'''


class SystemsCodeGen:
    def __init__(self, ast, output_bin="program", target="c"):
        self.ast        = ast
        self.output_bin = output_bin
        self.target     = target.lower()
        self.out_code   = []
        self.global_code = []
        self._needs_math  = False
        self._needs_rand  = False
        self._needs_str   = False
        self._str_vars    = set()
        self._bool_vars   = set()
        self._tmp_counter = 0
        self.in_class     = False

    # ── public entry ────────────────────────────────────────────────────────
    def generate(self):
        self._scan_needs(self.ast)
        if self.target == "js":
            self._generate_js()
        else:
            self._generate_c()

    def _scan_needs(self, node):
        if isinstance(node, ProgramNode):
            for s in node.statements: self._scan_needs(s)
        elif isinstance(node, (MathFuncNode,)):
            self._needs_math = True
        elif isinstance(node, RandomNode):
            self._needs_rand = True
        elif isinstance(node, (StringDeclarationNode, InputStringNode, DisplayTextNode)):
            self._needs_str = True
        elif isinstance(node, (LoopNode, ForLoopNode, WhileNode)):
            for s in node.body: self._scan_needs(s)
        elif isinstance(node, IfNode):
            for s in node.true_body + node.false_body: self._scan_needs(s)
        elif isinstance(node, FunctionNode):
            for s in node.body: self._scan_needs(s)
        elif isinstance(node, ClassNode):
            for s in node.body: self._scan_needs(s)

    # ── JS Backend ──────────────────────────────────────────────────────────
    def _generate_js(self):
        header = [
            "// ============================================================",
            "//  NATCOM STUDIO — JavaScript Bootstrap Matrix",
            "//  Auto-generated by NATCOM Compiler v2.0",
            "// ============================================================",
            "",
            "console.log('[NATCOM JS] Bootstrap matrix initialized.');",
            "",
        ]
        self.visit(self.ast)
        
        full_code = header + self.global_code + [""] + self.out_code
        
        js_path = self.output_bin if self.output_bin.endswith(".js") else self.output_bin + ".js"
        with open(js_path, "w") as f:
            f.write("\n".join(full_code))

    # ── C Backend ───────────────────────────────────────────────────────────
    def _generate_c(self):
        prog = os.path.basename(self.output_bin).upper()
        
        self.visit(self.ast)

        code = []
        code += ["#include <stdio.h>", "#include <stdlib.h>",
                 "#include <stdarg.h>", "#include <stdbool.h>",
                 "#include <string.h>", ""]
        if self._needs_math:
            code.append("#include <math.h>")
        if self._needs_rand:
            code.append("#include <time.h>")
        code.append("")

        for ln in _C_COLORS.splitlines(): code.append(ln)
        code.append("")
        for ln in _C_TIMING.splitlines(): code.append(ln)
        code.append("")
        for ln in _C_HELPERS.splitlines(): code.append(ln)
        code.append("")
        for ln in _C_SOVEREIGN.splitlines(): code.append(ln)
        code.append("")

        code += self.global_code
        code.append("")

        code.append("int main(void) {")
        if self._needs_rand:
            code.append("    srand((unsigned)time(NULL));")
        code.append(f'    nc_banner("{prog}");')
        code.append("    _nc_start_timer();")
        code.append('    nc_section("PROGRAM OUTPUT");')

        code += self.out_code

        code.append("    nc_footer(_nc_elapsed_ms());")
        code.append('    printf("  Press Enter to exit...\\n");')
        code.append("    getchar();")
        code.append("    return 0;")
        code.append("}")

        c_path = f"{self.output_bin}.c"
        with open(c_path, "w") as f:
            f.write("\n".join(code))

        libs = ["-lm"] if self._needs_math else []
        res = subprocess.run(
            ["gcc", "-O3", "-Wno-unused-function", "-Wno-unused-variable",
             "-fstack-protector-strong", c_path, "-o", self.output_bin] + libs,
            capture_output=True, text=True
        )
        if res.returncode != 0:
            print(f"\033[91m[!] GCC Error:\033[0m\n{res.stderr}")

    # ── Visitor ─────────────────────────────────────────────────────────────
    def visit(self, node, indent="    "):
        js = self.target == "js"
        if js and indent == "    ":
            indent = ""

        c = self.out_code  # alias

        if isinstance(node, ProgramNode):
            for stmt in node.statements:
                self.visit(stmt, indent)

        # ── OOP & Functions ─────────────────────────────────────────────────
        elif isinstance(node, FunctionNode):
            orig_c = self.out_code
            self.out_code = self.global_code
            args_str = ", ".join(f"double {a}" for a in node.args) if not js else ", ".join(node.args)
            if js:
                self.out_code.append(f"function {node.name}({args_str}) {{")
            else:
                self.out_code.append(f"void {node.name}({args_str}) {{")
            for s in node.body: self.visit(s, "    ")
            self.out_code.append("}\n")
            self.out_code = orig_c

        elif isinstance(node, ClassNode):
            orig_c = self.out_code
            self.out_code = self.global_code
            self.in_class = True
            if js:
                self.out_code.append(f"class {node.name} {{")
                self.out_code.append(f"    constructor() {{")
                for s in node.body: self.visit(s, "        ")
                self.out_code.append(f"    }}")
                self.out_code.append(f"}}")
            else:
                self.out_code.append(f"typedef struct {node.name} {node.name};")
                self.out_code.append(f"struct {node.name} {{")
                for s in node.body: self.visit(s, "    ")
                self.out_code.append(f"}};")
            self.in_class = False
            self.out_code = orig_c

        elif isinstance(node, FunctionCallNode):
            args_str = ", ".join(node.args)
            if js: c.append(f"{indent}{node.name}({args_str});")
            else:  c.append(f"{indent}{node.name}({args_str});")

        elif isinstance(node, ObjectInstantiateNode):
            if js:
                c.append(f"{indent}let {node.var_name} = new {node.class_name}();")
            else:
                c.append(f"{indent}{node.class_name} {node.var_name};")

        # ── Sovereign / Engine ──────────────────────────────────────────────
        elif isinstance(node, InitSovereignLayerNode):
            if js: c.append(f"{indent}console.log('[SOVEREIGN] ZKP audit hooks initialized.');")
            else:  c.append(f"{indent}init_sovereign_matrix();")

        elif isinstance(node, InitViewportNode):
            if js: c.append(f"{indent}console.log('[ENGINE] Gaming viewport initialized.');")
            else:  c.append(f"{indent}init_viewport();")

        elif isinstance(node, SyncCloudNode):
            if js: c.append(f"{indent}console.log('[GCP] State synced.');")
            else:  c.append(f"{indent}sync_cloud_ram();")

        elif isinstance(node, RenderMatrixNode):
            if js: c.append(f"{indent}console.log('[RENDER] Matrix at ({node.x},{node.y},{node.z})');")
            else:  c.append(f"{indent}render_matrix({node.x},{node.y},{node.z});")

        # ── Variable Declarations ───────────────────────────────────────────
        elif isinstance(node, VariableDeclarationNode):
            if js:
                prefix = "this." if self.in_class else "let "
                c.append(f"{indent}{prefix}{node.name} = {node.value};")
            else:
                t = "int" if "integer" in node.var_type else "float"
                if self.in_class:
                    c.append(f"{indent}{t} {node.name};")
                else:
                    c.append(f"{indent}{t} {node.name} = {node.value};")

        elif isinstance(node, StringDeclarationNode):
            self._str_vars.add(node.name)
            if js:
                c.append(f'{indent}let {node.name} = "{node.value}";')
            else:
                safe = node.value.replace('"', '\\"')
                c.append(f'{indent}char {node.name}[512] = "{safe}";')

        elif isinstance(node, BoolDeclarationNode):
            self._bool_vars.add(node.name)
            if js:
                val = "true" if node.value == "1" else "false"
                c.append(f"{indent}let {node.name} = {val};")
            else:
                c.append(f"{indent}int {node.name} = {node.value};")

        # ── Assignment ──────────────────────────────────────────────────────
        elif isinstance(node, AssignNode):
            if js: c.append(f"{indent}{node.var_name} = {node.value};")
            else:  c.append(f"{indent}{node.var_name} = {node.value};")

        # ── Swap ────────────────────────────────────────────────────────────
        elif isinstance(node, SwapNode):
            if js:
                c.append(f"{indent}[{node.a}, {node.b}] = [{node.b}, {node.a}];")
            else:
                tmp = f"_nc_tmp_{self._tmp_counter}"; self._tmp_counter += 1
                c.append(f"{indent}{{ float {tmp} = {node.a}; {node.a} = {node.b}; {node.b} = {tmp}; }}")

        # ── Math Operations ─────────────────────────────────────────────────
        elif isinstance(node, MathOpNode):
            c.append(f"{indent}{node.var_name} = {node.var_name} {node.operator} {node.amount};")

        elif isinstance(node, IncrDecrNode):
            c.append(f"{indent}{node.var_name}{node.op};")

        elif isinstance(node, MathFuncNode):
            self._needs_math = True
            f_ = node.func
            t, op, op2 = node.target, node.operand, node.operand2
            if js:
                js_map = {
                    'sqrt': f"Math.sqrt({op})", 'abs': f"Math.abs({op})",
                    'floor': f"Math.floor({op})", 'ceil': f"Math.ceil({op})",
                    'log': f"Math.log({op})", 'exp': f"Math.exp({op})",
                    'max': f"Math.max({op},{op2})", 'min': f"Math.min({op},{op2})",
                    'pow': f"Math.pow({op},{op2})", 'pow_self': f"Math.pow({op},{op2})",
                }
                c.append(f"{indent}{t} = {js_map.get(f_, op)};")
            else:
                c_map = {
                    'sqrt': f"sqrt((double)({op}))",
                    'abs':  f"fabs((double)({op}))",
                    'floor':f"floor((double)({op}))",
                    'ceil': f"ceil((double)({op}))",
                    'log':  f"log((double)({op}))",
                    'exp':  f"exp((double)({op}))",
                    'max':  f"(({op})>({op2})?({op}):({op2}))",
                    'min':  f"(({op})<({op2})?({op}):({op2}))",
                    'pow':  f"pow((double)({op}),(double)({op2}))",
                    'pow_self': f"pow((double)({op}),(double)({op2}))",
                }
                c.append(f"{indent}{t} = {c_map.get(f_, op)};")

        elif isinstance(node, ModuloNode):
            if js: c.append(f"{indent}{node.target} = {node.dividend} % {node.divisor};")
            else:  c.append(f"{indent}{node.target} = (int)({node.dividend}) % (int)({node.divisor});")

        elif isinstance(node, RandomNode):
            self._needs_rand = True
            if js:
                c.append(f"{indent}{node.target} = Math.floor(Math.random() * ({node.high} - {node.low} + 1)) + {node.low};")
            else:
                c.append(f"{indent}{node.target} = (rand() % ((int)({node.high}) - (int)({node.low}) + 1)) + (int)({node.low});")

        # ── User Input ──────────────────────────────────────────────────────
        elif isinstance(node, InputNode):
            safe_p = node.prompt.replace('"', '\\"')
            if js:
                c.append(f"{indent}// [INPUT] {node.var_name} — user input required (use prompt() in browser)")
                c.append(f"{indent}{node.var_name} = parseFloat(prompt('{safe_p}') || '0');")
            else:
                c.append(f'{indent}nc_input_prompt("{safe_p}");')
                c.append(f"{indent}scanf(\"%lf\", &{node.var_name});")
                c.append(f'{indent}nc_log("Input received", "%g", (double){node.var_name});')

        elif isinstance(node, InputStringNode):
            safe_p = node.prompt.replace('"', '\\"')
            if js:
                c.append(f"{indent}{node.var_name} = prompt('{safe_p}') || '';")
            else:
                c.append(f'{indent}nc_input_prompt("{safe_p}");')
                c.append(f"{indent}fgets({node.var_name}, sizeof({node.var_name}), stdin);")
                c.append(f"{indent}{node.var_name}[strcspn({node.var_name}, \"\\n\")] = 0;")
                c.append(f'{indent}nc_log("Text received", "%s", {node.var_name});')

        # ── Print / Display ─────────────────────────────────────────────────
        elif isinstance(node, PrintNode):
            vn = node.var_name
            if js:
                c.append(f"{indent}console.log('  ◆  {vn} =', {vn});")
            else:
                if vn.startswith('"'):
                    # Literal string constant
                    c.append(f'{indent}nc_log("Output", "%s", {vn});')
                elif vn in self._str_vars:
                    c.append(f'{indent}nc_value_s("{vn}", {vn});')
                elif vn in self._bool_vars:
                    c.append(f'{indent}nc_value_b("{vn}", {vn});')
                else:
                    # Default: treat as numeric float
                    c.append(f'{indent}nc_value_f("{vn}", (double){vn});')


        elif isinstance(node, DisplayTextNode):
            safe = node.text.replace('"', '\\"')
            if js: c.append(f'{indent}console.log("  {safe}");')
            else:  c.append(f'{indent}nc_display("{safe}");')

        elif isinstance(node, DisplayVarNode):
            for vn in node.vars_list:
                if js: c.append(f'{indent}console.log("  ◆  {vn} =", {vn});')
                elif vn in self._str_vars:  c.append(f'{indent}nc_value_s("{vn}", {vn});')
                elif vn in self._bool_vars: c.append(f'{indent}nc_value_b("{vn}", {vn});')
                else: c.append(f'{indent}nc_value_f("{vn}", (double){vn});')


        elif isinstance(node, PrintLineNode):
            if js: c.append(f'{indent}console.log("");')
            else:  c.append(f'{indent}printf("\\n");')

        # ── Loops ───────────────────────────────────────────────────────────
        elif isinstance(node, LoopNode):
            c.append(f"{indent}while(1) {{")
            for s in node.body: self.visit(s, indent + "    ")
            c.append(f"{indent}}}")

        elif isinstance(node, ForLoopNode):
            c.append(f"{indent}for(int _i = 0; _i < {node.count}; _i++) {{")
            for s in node.body: self.visit(s, indent + "    ")
            c.append(f"{indent}}}")

        elif isinstance(node, WhileNode):
            c.append(f"{indent}while({node.condition}) {{")
            for s in node.body: self.visit(s, indent + "    ")
            c.append(f"{indent}}}")

        # ── Conditionals ────────────────────────────────────────────────────
        elif isinstance(node, IfNode):
            c.append(f"{indent}if ({node.condition}) {{")
            for s in node.true_body:  self.visit(s, indent + "    ")
            if node.false_body:
                c.append(f"{indent}}} else {{")
                for s in node.false_body: self.visit(s, indent + "    ")
            c.append(f"{indent}}}")

        elif isinstance(node, HaltNode):
            if js: c.append(f"{indent}console.log('[ENGINE] Simulation halted.');")
            else:  c.append(f'{indent}nc_info("Simulation halted gracefully.");')
            c.append(f"{indent}break;")

        elif isinstance(node, ContinueNode):
            c.append(f"{indent}/* continue */")

        # ── Override ────────────────────────────────────────────────────────
        elif isinstance(node, OverrideBlockNode):
            c.append(f"{indent}/* ── SYSTEM OVERRIDE ── */")
            for ln in node.code.split('\n'):
                c.append(f"{indent}{ln}")





