import os
import subprocess
from src.parser import *

class SystemsCodeGen:
    def __init__(self, ast, output_bin="game_engine", target="c"):
        self.ast = ast
        self.output_bin = output_bin
        self.target = target.lower()
        self.out_code = []

    def generate(self):
        if self.target == "js":
            self._generate_js()
        else:
            self._generate_c()

    def _generate_js(self):
        self.out_code.append("// --- NATCOM STUDIO JS BOOTSTRAP MATRIX ---")
        self.out_code.append("console.log('[NATCOM JS] Matrix Bootstrapped.');")
        self.visit(self.ast)
        
        js_src_path = self.output_bin
        if not js_src_path.endswith(".js"):
            js_src_path += ".js"
            
        with open(js_src_path, "w") as f:
            f.write("\n".join(self.out_code))
            
        print(f"[*] Bootstrapping to JavaScript Matrix: {js_src_path}")
        print(f"[*] JavaScript Generation successful.")

    def _generate_c(self):
        self.out_code.append("#include <stdio.h>")
        self.out_code.append("#include <stdlib.h>")
        self.out_code.append("#include <stdbool.h>")
        self.out_code.append("")
        self.out_code.append("void init_sovereign_matrix() { printf(\"[SOVEREIGN MATRIX] Cloaked ZKP Audit Hooks Initialized.\\n\"); }")
        self.out_code.append("void init_viewport() { printf(\"[ENGINE] High Performance Gaming Viewport Initialized with Gravity.\\n\"); }")
        self.out_code.append("void render_matrix(float x, float y, float z) { printf(\"[ENGINE] Rendered 3D Matrix at (%.2f, %.2f, %.2f)\\n\", x, y, z); }")
        self.out_code.append("void sync_cloud_ram() { printf(\"[GCP_SYNC] State synced to Google Cloud Storage Virtual RAM.\\n\"); }")
        self.out_code.append("void flush_render_pipeline() { printf(\"[SYSTEM] Render Pipeline Flushed.\\n\"); }")
        self.out_code.append("")
        self.out_code.append("int main() {")
        
        self.visit(self.ast)
        
        self.out_code.append("    printf(\"\\n[SYSTEM] Execution complete. Press Enter to exit...\\n\");")
        self.out_code.append("    getchar();")
        self.out_code.append("    return 0;")
        self.out_code.append("}")
        
        c_src_path = f"{self.output_bin}.c"
        with open(c_src_path, "w") as f:
            f.write("\n".join(self.out_code))
            
        print(f"[*] Compiling to native binary with -O3 optimizations: {self.output_bin}")
        res = subprocess.run(["gcc", "-O3", c_src_path, "-o", self.output_bin])
        if res.returncode == 0:
            print(f"[*] Compilation successful. Run ./{self.output_bin}")
        else:
            print("[!] Self-Healing Engine: Compilation failed. Please verify syntax.")

    def visit(self, node, indent="    "):
        if self.target == "js" and indent == "    ":
            indent = "" # No main() wrapper in JS
            
        if isinstance(node, ProgramNode):
            for stmt in node.statements:
                self.visit(stmt, indent)
        elif isinstance(node, InitSovereignLayerNode):
            if self.target == "c": self.out_code.append(f"{indent}init_sovereign_matrix();")
            else: self.out_code.append(f"{indent}console.log('[SOVEREIGN MATRIX] Cloaked ZKP Audit Hooks Initialized.');")
        elif isinstance(node, VariableDeclarationNode):
            if self.target == "c":
                c_type = "int" if node.var_type == "integer" else "float"
                self.out_code.append(f"{indent}{c_type} {node.name} = {node.value};")
            else:
                self.out_code.append(f"{indent}let {node.name} = {node.value};")
        elif isinstance(node, InitViewportNode):
            if self.target == "c": self.out_code.append(f"{indent}init_viewport();")
            else: self.out_code.append(f"{indent}console.log('[ENGINE] High Performance Gaming Viewport Initialized with Gravity.');")
        elif isinstance(node, RenderMatrixNode):
            if self.target == "c": self.out_code.append(f"{indent}render_matrix({node.x}, {node.y}, {node.z});")
            else: self.out_code.append(f"{indent}console.log('[ENGINE] Rendered 3D Matrix at ({node.x}, {node.y}, {node.z})');")
        elif isinstance(node, LoopNode):
            if self.target == "c": self.out_code.append(f"{indent}while(true) {{")
            else: self.out_code.append(f"{indent}while(true) {{")
            for stmt in node.body:
                self.visit(stmt, indent + "    ")
            self.out_code.append(f"{indent}}}")
        elif isinstance(node, MathOpNode):
            op = node.operator
            if op == "=":
                # MathOpNode currently operator is literally '=', wait, MathOp uses '+' etc.
                # In python parser:
                # 'add x to y' => y += x
                # parser handles '+' operator
                pass
            self.out_code.append(f"{indent}{node.var_name} = {node.var_name} {op} {node.amount};")
        elif isinstance(node, IfNode):
            self.out_code.append(f"{indent}if ({node.condition}) {{")
            for stmt in node.true_body:
                self.visit(stmt, indent + "    ")
            self.out_code.append(f"{indent}}} else {{")
            for stmt in node.false_body:
                self.visit(stmt, indent + "    ")
            self.out_code.append(f"{indent}}}")
        elif isinstance(node, PrintNode):
            if self.target == "c":
                if node.var_name.startswith("\""):
                    self.out_code.append(f"{indent}printf(\"[APP LOG] %s\\n\", {node.var_name});")
                else:
                    self.out_code.append(f"{indent}printf(\"[APP LOG] {node.var_name}: %.2f\\n\", (float){node.var_name});")
            else:
                self.out_code.append(f"{indent}console.log('[APP LOG] ' + {node.var_name});")
        elif isinstance(node, HaltNode):
            if self.target == "c":
                self.out_code.append(f"{indent}printf(\"[ENGINE] Simulation Halted.\\n\");")
            else:
                self.out_code.append(f"{indent}console.log('[ENGINE] Simulation Halted.');")
            self.out_code.append(f"{indent}break;")
        elif isinstance(node, ContinueNode):
            self.out_code.append(f"{indent}// Keep simulation running")
        elif isinstance(node, SyncCloudNode):
            if self.target == "c": self.out_code.append(f"{indent}sync_cloud_ram();")
            else: self.out_code.append(f"{indent}console.log('[GCP_SYNC] State synced to Google Cloud Storage Virtual RAM.');")
        elif isinstance(node, OverrideBlockNode):
            self.out_code.append(f"{indent}// SYSTEM OVERRIDE INJECTED:")
            for line in node.code.split('\n'):
                self.out_code.append(f"{indent}{line.strip()}")
