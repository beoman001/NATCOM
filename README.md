# NATCOM — Natural Communication Language

> **Code in plain English. No syntax. No barriers.**

<div align="center">

![NATCOM Logo](ui/natcom_icon.png)

**NATCOM** is the world's first **English-only programming language**.  
Write programs in natural English sentences — NATCOM compiles them to blazing-fast native C binaries or JavaScript.

[![Version](https://img.shields.io/badge/version-2.0-00ffcc?style=flat-square)](#)
[![Language](https://img.shields.io/badge/language-English-7c6af7?style=flat-square)](#)
[![Target](https://img.shields.io/badge/target-Native%20C%20%7C%20JavaScript-f7a06a?style=flat-square)](#)
[![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)](#)

**Created by [Beon Binesh](ui/about.html) · Developed with Google Gemini & Antigravity AGY**

</div>

---

## 🚀 Quick Start

### 1. Install
```bash
git clone https://github.com/beoboy/NATCOM.git
cd NATCOM
chmod +x natcom
```

### 2. Write your first program (`hello.nc`)
```
Create a string named Greeting and set it to "Hello, World!".
Display "Welcome to NATCOM — The English Programming Language!"
Log the value of Greeting.
```

### 3. Compile & Run
```bash
./natcom build hello.nc -o hello
./hello
```

### 4. Open NATCOM Studio (Web IDE)
```bash
python3 server.py
# Open: http://localhost:8080
```

---

## 💡 Philosophy

Traditional programming forces you to learn **syntax rules** before solving real problems.  
NATCOM flips this — **you write English, the compiler does the translation**.

| Traditional (C) | NATCOM |
|---|---|
| `int score = 0;` | `Create a high speed integer named Score and set it to 0.` |
| `scanf("%f", &x);` | `Ask the user to enter a value for X.` |
| `result = sqrt(x);` | `Set Result to the square root of X.` |
| `for(int i=0;i<10;i++)` | `Repeat 10 times:` |
| `if (a > b) { ... }` | `If the A is greater than B, then:` |

---

## 📖 Complete Language Reference

### Variables

| Statement | Type |
|---|---|
| `Create a high speed integer named X and set it to 5.` | Integer |
| `Create a floating point variable named X and set it to 3.14.` | Float |
| `Create a string named Name and set it to "Hello".` | String (char[512]) |
| `Create a boolean named Flag and set it to true.` | Boolean (true/false) |
| `Set X to 42.` | Assignment |
| `Swap the values of X and Y.` | Swap two variables |

### User Input

```
Ask the user to enter a value for X.
Ask the user to enter a value for Speed with prompt 'Enter speed (m/s)'.
Ask the user for text named Name.
Ask the user to enter text for Address with prompt 'Your address'.
```

### Arithmetic

```
Add 10 to Score.
Subtract 5 from Score.
Multiply Score by 2.
Divide Score by 4.
Increase Health by 50.
Decrease Fuel by 10.
Increment Counter.
Decrement Counter.
Find the remainder of A divided by B and store in Result.
```

### Math Functions

```
Set Result to the square root of X.
Set Result to the absolute value of X.
Set Result to the floor of X.
Set Result to the ceiling of X.
Set Result to the natural log of X.
Set Result to e to the power of X.
Set Result to the maximum of A and B.
Set Result to the minimum of A and B.
Raise X to the power of Y.
Set Result to X to the power of Y.
Set X to a random number between 1 and 100.
Generate a random number between 1 and 100 and store in X.
```

### Output / Display

```
Log the value of X.
Display "Hello World".
Display 'Hello World'.
Display the value of X.
Display the values of X and Y and Z.
Print a blank line.
```

### Conditionals

```
If the X is greater than Y, then:
  Log the value of X.
Otherwise:
  Log the value of Y.
```

Supported operators: `is greater than`, `is less than`, `equals`, `is not`, `drops below`

### Loops

**Repeat Loop:**
```
Repeat 10 times:
  Increment Counter.
  Log the value of Counter.
Done.
```

**While Loop:**
```
Keep running while Counter is less than 10:
  Increment Counter.
Stop the loop.
```

**Simulation Loop (Game Loop):**
```
Begin the main simulation loop.
  Increase Score by 1.
  If the Score is greater than 100, then:
    Halt the simulation.
  Otherwise:
    Keep the simulation running.
```

### Sovereign Layer (Advanced)

```
Initialize the cloaked zero-knowledge matrix for sovereign auditing.
Initialize high performance gaming viewport with gravity physics.
Render a 3D matrix representing a vehicle at coordinates 10.5, 50.0, 15.2.
Sync the current game state to Google Cloud Storage virtual RAM expansion using safe offline fallbacks.
```

### Raw Code Override

Embed raw C or JavaScript directly inside your English program:

```
<SYSTEM_OVERRIDE>
printf("Raw C code here\n");
int raw_var = 42;
</SYSTEM_OVERRIDE>
```

### Comments

```
// This is a comment — ignored by the compiler
```

---

## 🔨 Compiler CLI

```bash
# Compile to native binary (default)
./natcom build file.nc -o output

# Compile to JavaScript
./natcom build file.nc --target js -o output.js

# Build examples
./natcom build examples/calculator.nc -o calculator
./natcom build examples/full_demo.nc -o full_demo
```

---

## 📂 Example Programs

### Hello World (`examples/hello.nc`)
```
Create a string named Greeting and set it to "Hello, World!".
Create a boolean named IsRunning and set it to true.
Create a high speed integer named Counter and set it to 0.

Display "Welcome to NATCOM!"
Log the value of Greeting.
Log the value of IsRunning.

Repeat 5 times:
  Increment Counter.
Done.

Log the value of Counter.
```

### Calculator with User Input (`examples/calculator.nc`)
```
Create a floating point variable named A and set it to 0.
Create a floating point variable named B and set it to 0.

Ask the user to enter a value for A.
Ask the user to enter a value for B.

Create a floating point variable named Sum and set it to 0.
Add A to Sum.
Add B to Sum.
Display the values of Sum.
```

### Budget Tracker (`examples/budget_tracker.nc`)
```
Create a floating point variable named Budget and set it to 0.
Create a floating point variable named Expenses and set it to 0.

Ask the user to enter a value for Budget.
Ask the user to enter a value for Expenses.

Create a floating point variable named Savings and set it to 0.
Add Budget to Savings.
Subtract Expenses from Savings.
Display the values of Savings.

If the Savings is greater than 0, then:
  Display "You saved money!"
Otherwise:
  Display "You are over budget!"
```

---

## 🌐 NATCOM Studio (Web IDE)

The built-in web IDE provides:
- ✅ **Syntax highlighting** — keywords colored by category
- ✅ **Live error detection** — red squiggles on unknown lines
- ✅ **Error suggestions** — intelligent fix suggestions per error
- ✅ **Error gutter** — red/yellow dots in the margin
- ✅ **Language reference** — click-to-insert cheatsheet sidebar
- ✅ **File explorer** — multi-tab editor
- ✅ **Examples library** — all examples built-in
- ✅ **Terminal output** — colored compilation output
- ✅ **Target switching** — Native C or JavaScript

```bash
python3 server.py      # Start on http://localhost:8080
```

---

## 🏗 Architecture

```
NATCOM/
├── natcom              # CLI compiler entry point
├── server.py           # Web IDE backend (Python, no dependencies)
├── src/
│   ├── lexer.py        # Free-form English tokenizer
│   ├── parser.py       # MultiverseParser + Self-Healing Engine
│   └── codegen.py      # Multi-target code generator (C + JS)
├── ui/
│   ├── index.html      # NATCOM Studio IDE
│   ├── style.css       # Premium dark theme
│   ├── script.js       # IDE logic + syntax highlighter
│   └── about.html      # Creator page — Beon Binesh
└── examples/
    ├── hello.nc
    ├── calculator.nc
    ├── budget_tracker.nc
    ├── counter.nc
    ├── game_physics.nc
    └── full_demo.nc
```

---

## 👤 Created By

**Beon Binesh**  
Software Architect · Language Designer · AI Pioneer

Developed with **Google Gemini 2.5** and **Antigravity AGY** (Google DeepMind)

> [View Creator Page →](ui/about.html)

---

## 📜 License

MIT License · © 2026 Beon Binesh
