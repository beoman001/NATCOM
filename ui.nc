// ui.nc - NATCOM STUDIO UI LOGIC 
// Compiled natively to JavaScript via NATCOM V2 JS Backend

// Bootstrapped State Initialization (Compiles natively to JS let)
Initialize the cloaked zero-knowledge matrix for sovereign auditing.
Create a high speed integer named CompilationAttempts and set it to 0.

<SYSTEM_OVERRIDE>
document.addEventListener('DOMContentLoaded', () => {
    const compileBtn = document.getElementById('compileBtn');
    const clearBtn = document.getElementById('clearBtn');
    const editor = document.getElementById('editor');
    const terminal = document.getElementById('terminal');

    function appendLog(text, type = 'output') {
        const lines = text.split('\n');
        lines.forEach(line => {
            if (!line.trim()) return;
            const div = document.createElement('div');
            div.className = `log ${type}`;
            div.textContent = line;
            terminal.appendChild(div);
        });
        terminal.scrollTop = terminal.scrollHeight;
    }

    clearBtn.addEventListener('click', () => {
        terminal.innerHTML = '';
        appendLog('Terminal cleared.', 'system');
    });

    compileBtn.addEventListener('click', async () => {
        const code = editor.value;
        if (!code.trim()) return;

        // Utilizing native NATCOM variables compiled globally
        CompilationAttempts += 1;

        compileBtn.classList.add('loading');
        compileBtn.innerHTML = 'COMPILING...';
        
        appendLog(`\n--- INITIATING COMPILATION SEQUENCE (ATTEMPT #${CompilationAttempts}) ---`, 'system');

        try {
            const response = await fetch('/compile', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ code })
            });

            const data = await response.json();
            
            if (data.output) {
                const outputStr = data.output;
                if (outputStr.includes('Compilation failed') || outputStr.includes('Syntax Anomaly')) {
                    appendLog(outputStr, 'error');
                } else if (outputStr.includes('Total Independence') || outputStr.includes('Compilation successful')) {
                    appendLog(outputStr, 'success');
                } else {
                    appendLog(outputStr, 'output');
                }
            } else {
                appendLog('No output received from native matrix.', 'system');
            }
        } catch (err) {
            appendLog(`[NETWORK ERROR] Failed to reach Sovereign Layer: ${err.message}`, 'error');
        } finally {
            compileBtn.classList.remove('loading');
            compileBtn.innerHTML = `
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M5 3L19 12L5 21V3Z" fill="currentColor"/>
                </svg>
                COMPILE & EXECUTE
            `;
        }
    });
    
    // Tab support in textarea
    editor.addEventListener('keydown', function(e) {
        if (e.key === 'Tab') {
            e.preventDefault();
            const start = this.selectionStart;
            const end = this.selectionEnd;
            this.value = this.value.substring(0, start) + "    " + this.value.substring(end);
            this.selectionStart = this.selectionEnd = start + 4;
        }
    });
});
</SYSTEM_OVERRIDE>
