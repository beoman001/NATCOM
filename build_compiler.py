import os

compiler_files = ['natcom', 'src/lexer.py', 'src/parser.py', 'src/codegen.py', 'server.py', 'ui/index.html', 'ui/style.css', 'ui/about.html']

c_code = [
    '    printf("[BOOTSTRAP V2] Rebuilding Sovereign NATCOM Engine...\\n");',
    '    system("mkdir -p src");',
    '    system("mkdir -p ui");'
]

for f in compiler_files:
    with open(f, 'r') as file:
        content = file.read()
    
    # We escape double quotes and backslashes for the C string literal.
    # The shell handles the heredoc.
    content_escaped = content.replace('\\', '\\\\').replace('"', '\\"').replace('$', '\\$').replace('`', '\\`')
    # Because this is passed to C system("..."), we need to escape newlines inside the string literal!
    c_cmd = f'cat << \\\'EOF_NATCOM_BOOTSTRAP\\\' > {f}\\n{content_escaped}\\nEOF_NATCOM_BOOTSTRAP'
    c_cmd = c_cmd.replace('\n', '\\n')
    c_code.append(f'    system("{c_cmd}");')

if 'natcom' in compiler_files:
    c_code.append('    system("chmod +x natcom");')
    
c_code.append('    printf("[BOOTSTRAP V2] Rebuild Complete. All systems sovereign.\\n");')

nc_header = '''// compiler.nc — NATCOM Self-Bootstrapped Engine
// This file natively compiles to a C executable that reconstructs the entire Python NATCOM toolchain.
Initialize the cloaked zero-knowledge matrix for sovereign auditing.

<SYSTEM_OVERRIDE>
'''

with open('compiler.nc', 'w') as out:
    out.write(nc_header)
    for c in c_code:
        out.write(c + '\n')
    out.write('</SYSTEM_OVERRIDE>\n')
