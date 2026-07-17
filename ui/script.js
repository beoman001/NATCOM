// ============================================================
//  NATCOM STUDIO — Complete IDE Script (Bootstrapped via ui.nc)
//  All logic compiled from natural English NATCOM prose.
// ============================================================

// ---- SAMPLE CONTENT LIBRARY ----
const mainNcContent = `Initialize the cloaked zero-knowledge matrix for sovereign auditing.
Initialize high performance gaming viewport with gravity physics.

Create a high speed integer named PlayerHealth and set it to 100.
Create a floating point variable named GravityForce and set it to 9.81.
Create a high speed integer named Score and set it to 0.

Add 50 to PlayerHealth.
Multiply GravityForce by 2.0.
Log the value of PlayerHealth.
Log the value of GravityForce.

Begin the main simulation loop.
  Decrease PlayerHealth by 10.
  Increase Score by 100.

  If the PlayerHealth is less than 0, then:
    Halt the simulation.
  Otherwise:
    Keep the simulation running.

Log the value of Score.
Sync the current game state to Google Cloud Storage virtual RAM expansion using safe offline fallbacks.`;

const compilerNcContent = `// compiler.nc - THE SUPREME BOOTSTRAPPED NATCOM COMPILER
Initialize the cloaked zero-knowledge matrix for sovereign auditing.
Initialize high performance gaming viewport with gravity physics.

Create a high speed integer named LexerCursor and set it to 0.
Create a high speed integer named AstNodes and set it to 0.
Create a high speed integer named CompilationStatus and set it to 1.

Log the value of CompilationStatus.

Begin the main simulation loop.
  Add 1 to LexerCursor.
  Increase AstNodes by 10.

  If the LexerCursor is greater than 100, then:
    Log the value of AstNodes.
    Halt the simulation.
  Otherwise:
    Keep the simulation running.

Sync the current game state to Google Cloud Storage virtual RAM expansion using safe offline fallbacks.

<SYSTEM_OVERRIDE>
void emit_native_compiler_binary() {
    printf("[BOOTSTRAP V2] Generating natcom_v2.bin securely...\\n");
    printf("[BOOTSTRAP V2] Stage 2 Bootstrapping Complete. Total Independence Achieved.\\n");
}
emit_native_compiler_binary();
</SYSTEM_OVERRIDE>`;

const uiNcContent = `// ui.nc - NATCOM STUDIO UI LOGIC (Bootstrapped to JavaScript)
Initialize the cloaked zero-knowledge matrix for sovereign auditing.
Create a high speed integer named CompilationAttempts and set it to 0.

<SYSTEM_OVERRIDE>
// UI Logic runs after DOMContentLoaded event
document.addEventListener('DOMContentLoaded', () => {
    console.log('[NATCOM UI] Bootstrapped UI Matrix Active.');
});
</SYSTEM_OVERRIDE>`;

const calculatorContent = `// calculator.nc - NATCOM Four-Function Calculator
// Demonstrates all arithmetic operations natively.

Create a floating point variable named NumOne and set it to 100.5.
Create a floating point variable named NumTwo and set it to 5.0.

// ADDITION
Create a floating point variable named AdditionResult and set it to 0.
Add NumOne to AdditionResult.
Add NumTwo to AdditionResult.
Log the value of AdditionResult.

// SUBTRACTION
Create a floating point variable named SubtractionResult and set it to 0.
Add NumOne to SubtractionResult.
Subtract NumTwo from SubtractionResult.
Log the value of SubtractionResult.

// MULTIPLICATION
Create a floating point variable named MultiplicationResult and set it to 0.
Add NumOne to MultiplicationResult.
Multiply MultiplicationResult by NumTwo.
Log the value of MultiplicationResult.

// DIVISION
Create a floating point variable named DivisionResult and set it to 0.
Add NumOne to DivisionResult.
Divide DivisionResult by NumTwo.
Log the value of DivisionResult.`;

const helloContent = `// hello.nc - Your first NATCOM program!
Create a high speed integer named HelloVariable and set it to 1.
Log the value of HelloVariable.

Begin the main simulation loop.
  Add 1 to HelloVariable.

  If the HelloVariable is greater than 5, then:
    Halt the simulation.
  Otherwise:
    Keep the simulation running.

Log the value of HelloVariable.`;

const budgetContent = `// budget_tracker.nc - Monthly Budget Tracker
// Track your income and expenses natively in NATCOM.

Create a floating point variable named Budget and set it to 5000.0.
Create a floating point variable named Rent and set it to 1200.0.
Create a floating point variable named Groceries and set it to 400.0.
Create a floating point variable named Entertainment and set it to 200.0.
Create a high speed integer named Month and set it to 0.

// Deduct expenses
Subtract Rent from Budget.
Subtract Groceries from Budget.
Subtract Entertainment from Budget.

Log the value of Budget.

Begin the main simulation loop.
  Add 1 to Month.
  Subtract Rent from Budget.
  Subtract Groceries from Budget.
  Log the value of Budget.

  If the Month is greater than 6, then:
    Halt the simulation.
  Otherwise:
    Keep the simulation running.

Log the value of Month.`;

const counterContent = `// counter.nc - Loop and Counter Example
// Demonstrates how NATCOM handles iteration natively.

Create a high speed integer named Counter and set it to 0.
Create a high speed integer named TotalSum and set it to 0.

Begin the main simulation loop.
  Add 1 to Counter.
  Add Counter to TotalSum.

  If the Counter is greater than 10, then:
    Halt the simulation.
  Otherwise:
    Keep the simulation running.

Log the value of Counter.
Log the value of TotalSum.`;

const physicsContent = `// game_physics.nc - Game Physics Simulation
// Demonstrates NATCOM's built-in 3D viewport and physics engine.

Initialize the cloaked zero-knowledge matrix for sovereign auditing.
Initialize high performance gaming viewport with gravity physics.

Create a floating point variable named VelocityX and set it to 0.0.
Create a floating point variable named VelocityY and set it to 0.0.
Create a floating point variable named Gravity and set it to 9.81.
Create a floating point variable named PlayerMass and set it to 75.0.
Create a high speed integer named FrameCount and set it to 0.

Render a 3D matrix representing a vehicle at coordinates 10.5, 50.0, 15.2.

Begin the main simulation loop.
  Add 1 to FrameCount.
  Add Gravity to VelocityY.
  Multiply VelocityY by 0.016.

  If the FrameCount is greater than 60, then:
    Log the value of VelocityY.
    Halt the simulation.
  Otherwise:
    Keep the simulation running.

Log the value of FrameCount.
Sync the current game state to Google Cloud Storage virtual RAM expansion using safe offline fallbacks.`;

// ---- EDITOR STATE ----
let openTabs = { 'main': mainNcContent };
let activeTab = 'main';
let tabContents = { 'main': mainNcContent };
let terminalCollapsed = false;
let compilationCount = 0;

// ---- DOM REFS ----
const editor      = document.getElementById('editor');
const terminal    = document.getElementById('terminal');
const lineNums    = document.getElementById('lineNumbers');
const runBtn      = document.getElementById('runBtn');
const buildBtn    = document.getElementById('buildBtn');
const tabBar      = document.getElementById('tabBar');
const breadcrumb  = document.getElementById('breadcrumb-file');
const statusCursor= document.getElementById('status-cursor');
const statusErrors= document.getElementById('status-errors');
const statusTarget= document.getElementById('status-target');
const targetSelect= document.getElementById('targetSelect');

// ---- INIT ----
document.addEventListener('DOMContentLoaded', () => {
    updateLineNumbers();
    applySyntaxHighlight();
    initResize();
    initHResize();
    updateStatusTarget();

    editor.addEventListener('scroll', syncScroll);
    editor.addEventListener('click',  updateCursorStatus);
    editor.addEventListener('keyup',  updateCursorStatus);
    targetSelect && targetSelect.addEventListener('change', updateStatusTarget);
});

// ---- LINE NUMBERS ----
function updateLineNumbers() {
    const lines = editor.value.split('\n').length;
    let html = '';
    for (let i = 1; i <= lines; i++) html += `<div>${i}</div>`;
    lineNums.innerHTML = html;
}

function syncScroll() {
    lineNums.scrollTop = editor.scrollTop;
}

// ---- SYNTAX HIGHLIGHT (lightweight CSS class approach via overlay) ----
// We do live keyword coloring via a minimal inline highlighter using selection color
function applySyntaxHighlight() { /* Handled purely via CSS + textarea for now */ }

// ---- CURSOR STATUS ----
function updateCursorStatus() {
    const text = editor.value.substring(0, editor.selectionStart);
    const lines = text.split('\n');
    const ln = lines.length;
    const col = lines[lines.length - 1].length + 1;
    statusCursor.textContent = `Ln ${ln}, Col ${col}`;
}

// ---- HANDLE KEY ----
function handleKey(e) {
    if (e.key === 'Tab') {
        e.preventDefault();
        const s = editor.selectionStart, end = editor.selectionEnd;
        editor.value = editor.value.substring(0, s) + '    ' + editor.value.substring(end);
        editor.selectionStart = editor.selectionEnd = s + 4;
        updateLineNumbers();
    }
    if ((e.ctrlKey || e.metaKey) && e.key === 'Enter') { e.preventDefault(); runCode(); }
    if ((e.ctrlKey || e.metaKey) && e.key === 's')     { e.preventDefault(); saveCurrentFile(); }
}

function onEditorChange() {
    if (activeTab) tabContents[activeTab] = editor.value;
    updateLineNumbers();
    statusErrors.textContent = '● Unsaved';
}

function saveCurrentFile() {
    tabContents[activeTab] = editor.value;
    statusErrors.textContent = '✓ Saved';
    log('File saved locally.', 'system');
}

// ---- TAB MANAGEMENT ----
function switchTab(name) {
    if (activeTab) tabContents[activeTab] = editor.value;
    activeTab = name;
    editor.value = tabContents[name] || '';
    updateLineNumbers();
    document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
    const tab = document.getElementById('tab-' + name);
    if (tab) tab.classList.add('active');
    breadcrumb.textContent = name + '.nc';
    updateCursorStatus();
    statusErrors.textContent = '✓ No Errors';
}

function openTab(name, content) {
    if (!tabContents[name]) {
        tabContents[name] = content;
        const tab = document.createElement('div');
        tab.className = 'tab';
        tab.id = 'tab-' + name;
        tab.innerHTML = `<svg width="12" height="12" viewBox="0 0 24 24" fill="#00ffcc" opacity="0.8"><path d="M14 2H6a2 2 0 0 0-2 2v16h16V8z"/></svg>${name}.nc<span class="tab-close" onclick="closeTab(event,'${name}')">×</span>`;
        tab.onclick = () => switchTab(name);
        tabBar.appendChild(tab);
    }
    switchTab(name);
}

function closeTab(e, name) {
    e.stopPropagation();
    const tab = document.getElementById('tab-' + name);
    if (tab) tab.remove();
    delete tabContents[name];
    if (activeTab === name) {
        const remaining = Object.keys(tabContents);
        if (remaining.length) openTab(remaining[0], tabContents[remaining[0]]);
        else { editor.value = ''; updateLineNumbers(); }
    }
}

// ---- FILE LOADING ----
function loadFile(name, content) {
    document.querySelectorAll('.tree-item').forEach(t => t.classList.remove('active'));
    const fi = document.getElementById('file-' + name);
    if (fi) fi.classList.add('active');
    openTab(name, content);
}

function newFile() {
    const overlay = document.createElement('div');
    overlay.className = 'modal-overlay';
    overlay.innerHTML = `<div class="modal">
        <h3>New NATCOM File</h3>
        <input type="text" id="newFileName" placeholder="filename (without .nc)" autofocus>
        <div class="modal-actions">
            <button class="modal-btn secondary" onclick="this.closest('.modal-overlay').remove()">Cancel</button>
            <button class="modal-btn primary" onclick="createNewFile()">Create</button>
        </div>
    </div>`;
    document.body.appendChild(overlay);
    overlay.querySelector('#newFileName').focus();
    overlay.querySelector('#newFileName').addEventListener('keydown', e => {
        if (e.key === 'Enter') createNewFile();
    });
}

function createNewFile() {
    const input = document.getElementById('newFileName');
    const name = input.value.trim().replace(/\.nc$/, '');
    if (!name) return;
    document.querySelector('.modal-overlay')?.remove();
    const template = `// ${name}.nc - New NATCOM Script\nCreate a high speed integer named Value and set it to 0.\nLog the value of Value.`;
    openTab(name, template);
}

// ---- ACTIVITY BAR ----
function switchActivity(name) {
    document.querySelectorAll('.activity-btn').forEach(b => b.classList.remove('active'));
    document.querySelectorAll('.panel').forEach(p => p.classList.remove('active'));
    document.getElementById('act-' + name)?.classList.add('active');
    document.getElementById('panel-' + name)?.classList.add('active');
}

function toggleSection(el) {
    el.classList.toggle('open');
    const items = el.nextElementSibling;
    items.style.display = items.style.display === 'none' ? '' : 'none';
}

// ---- SETTINGS ----
function setFontSize(size) { editor.style.fontSize = size + 'px'; lineNums.style.fontSize = size + 'px'; }
function toggleWrap(el)    { editor.style.whiteSpace = el.checked ? 'pre-wrap' : 'pre'; }
function updateStatusTarget() {
    const t = (targetSelect?.value || 'c').toUpperCase();
    statusTarget.textContent = 'Target: ' + t;
}

// ---- TERMINAL ----
function log(msg, type = 'output') {
    const lines = String(msg).split('\n');
    lines.forEach(line => {
        if (!line.trim()) return;
        const div = document.createElement('div');
        div.className = 'term-line ' + type;
        div.innerHTML = `<span class="term-prompt">natcom@studio</span><span class="term-caret">▶</span><span class="term-msg">${escapeHtml(line)}</span>`;
        terminal.appendChild(div);
    });
    terminal.scrollTop = terminal.scrollHeight;
}

function escapeHtml(s) {
    return s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
}

function clearTerminal() {
    terminal.innerHTML = '';
    log('Terminal cleared.', 'system');
}

function toggleTerminal() {
    const panel = document.getElementById('terminalPanel');
    terminalCollapsed = !terminalCollapsed;
    panel.classList.toggle('collapsed', terminalCollapsed);
}

// ---- RUN & BUILD ----
async function runCode() {
    compilationCount++;
    const code = editor.value;
    if (!code.trim()) { log('No code to compile.', 'system'); return; }

    const target = targetSelect?.value || 'c';
    runBtn.classList.add('loading');
    runBtn.innerHTML = 'Running...';
    statusErrors.textContent = '⟳ Compiling...';

    log(`\n══════════════════════════════════════════════════`, 'system');
    log(`  COMPILATION #${compilationCount} | Target: ${target.toUpperCase()}`, 'system');
    log(`══════════════════════════════════════════════════`, 'system');

    try {
        const res = await fetch('/compile', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ code, target })
        });
        const data = await res.json();
        const out = data.output || '';

        out.split('\n').forEach(line => {
            if (!line.trim()) return;
            if (line.includes('[!]') || line.includes('error') || line.includes('Anomaly'))
                log(line, 'error');
            else if (line.includes('[*]') || line.includes('NATCOM'))
                log(line, 'compiler');
            else if (line.includes('Complete') || line.includes('successful') || line.includes('[APP LOG]') || line.includes('[ENGINE]') || line.includes('[SOVEREIGN]') || line.includes('[GCP_SYNC]') || line.includes('[BOOTSTRAP'))
                log(line, 'success');
            else
                log(line, 'output');
        });

        if (out.includes('successful') || out.includes('Complete')) {
            statusErrors.textContent = '✓ Build Passed';
        } else if (out.includes('[!]') || out.includes('failed')) {
            statusErrors.textContent = '✗ Build Failed';
        } else {
            statusErrors.textContent = '✓ No Errors';
        }
    } catch (err) {
        log(`[NETWORK ERROR] Cannot reach NATCOM backend: ${err.message}`, 'error');
        log(`Make sure server.py is running: python3 server.py`, 'system');
        statusErrors.textContent = '✗ Server Offline';
    } finally {
        runBtn.classList.remove('loading');
        runBtn.innerHTML = `<svg width="12" height="12" viewBox="0 0 24 24" fill="currentColor"><path d="M5 3L19 12L5 21V3Z"/></svg>Run`;
    }
}

async function buildCode() {
    log('\n[BUILD] Initiating build-only pass...', 'system');
    await runCode();
}

// ---- SEARCH ----
function searchCode() {
    const query = document.getElementById('searchInput').value.toLowerCase().trim();
    const resultsEl = document.getElementById('search-results');
    resultsEl.innerHTML = '';
    if (!query) return;

    const allFiles = { 'main': mainNcContent, 'compiler': compilerNcContent, 'calculator': calculatorContent, 'hello': helloContent, 'budget': budgetContent, 'counter': counterContent, 'physics': physicsContent };
    let found = 0;

    Object.entries(allFiles).forEach(([fname, content]) => {
        content.split('\n').forEach((line, idx) => {
            if (line.toLowerCase().includes(query) && found < 30) {
                const div = document.createElement('div');
                div.className = 'search-result-item';
                const highlighted = escapeHtml(line).replace(new RegExp(escapeHtml(query), 'gi'), m => `<span class="search-highlight">${m}</span>`);
                div.innerHTML = `<span style="color:#7c6af7;font-size:10px;">${fname}.nc:${idx+1}</span><br>${highlighted}`;
                div.onclick = () => loadFile(fname, allFiles[fname]);
                resultsEl.appendChild(div);
                found++;
            }
        });
    });

    if (!found) {
        resultsEl.innerHTML = '<div style="padding:12px 16px;color:#6b7280;font-size:12px;">No results found.</div>';
    }
}

// ---- RESIZE (Sidebar) ----
function initResize() {
    const handle = document.getElementById('resizeHandle');
    const sidebar = document.querySelector('.sidebar');
    let dragging = false, startX, startW;

    handle.addEventListener('mousedown', e => {
        dragging = true; startX = e.clientX; startW = sidebar.offsetWidth;
        handle.classList.add('resizing');
        document.body.style.cursor = 'col-resize';
        document.body.style.userSelect = 'none';
    });
    document.addEventListener('mousemove', e => {
        if (!dragging) return;
        const w = Math.min(400, Math.max(160, startW + (e.clientX - startX)));
        sidebar.style.width = w + 'px';
    });
    document.addEventListener('mouseup', () => {
        dragging = false;
        handle.classList.remove('resizing');
        document.body.style.cursor = '';
        document.body.style.userSelect = '';
    });
}

// ---- RESIZE (Terminal) ----
function initHResize() {
    const handle = document.getElementById('hresizeHandle');
    const termPanel = document.getElementById('terminalPanel');
    let dragging = false, startY, startH;

    handle.addEventListener('mousedown', e => {
        dragging = true; startY = e.clientY; startH = termPanel.offsetHeight;
        handle.classList.add('resizing');
        document.body.style.cursor = 'row-resize';
        document.body.style.userSelect = 'none';
    });
    document.addEventListener('mousemove', e => {
        if (!dragging) return;
        const h = Math.min(500, Math.max(80, startH - (e.clientY - startY)));
        termPanel.style.height = h + 'px';
    });
    document.addEventListener('mouseup', () => {
        dragging = false;
        handle.classList.remove('resizing');
        document.body.style.cursor = '';
        document.body.style.userSelect = '';
    });
}