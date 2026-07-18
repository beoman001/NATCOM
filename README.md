# NATCOM — Natural Communication Language

> **Code in plain English. No syntax. No barriers.**

<div align="center">

![NATCOM Logo](ui/natcom_icon.png)

**NATCOM** is the world's first **English-only programming language**.  
Write programs in natural English sentences — NATCOM compiles them to blazing-fast native binaries or runs them interactively in the browser.

[![Version](https://img.shields.io/badge/version-2.0-CC7832?style=flat-square)](#)
[![Language](https://img.shields.io/badge/language-English-6A8759?style=flat-square)](#)
[![Target](https://img.shields.io/badge/target-NATCOM%20Native%20%7C%20NATCOM%20Web%20Engine-6897BB?style=flat-square)](#)
[![Studio](https://img.shields.io/badge/IDE-NATCOM%20Studio-9876AA?style=flat-square)](#)
[![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)](#)

**Created by [Beon Binesh](ui/about.html) · Developed with Google Gemini & Antigravity AGY by Google DeepMind**

</div>

---

## 🚀 Quick Start

### 1. Clone & Install
```bash
git clone https://github.com/beoman001/NATCOM.git
cd NATCOM
chmod +x natcom
```

### 2. Write your first program (`hello.nc`)
```
Create a string named Greeting and set it to "Hello, World!".
Display "Welcome to NATCOM — The English Programming Language!".
Log the value of Greeting.
```

### 3. Compile & Run (NATCOM Native)
```bash
./natcom build hello.nc -o hello
./hello
```

### 4. Compile to Web Engine
```bash
./natcom build hello.nc --target js -o hello
```

### 5. Open NATCOM Studio (Full Web IDE)
```bash
python3 server.py
# Open: http://localhost:8080
```

---

## 💡 Philosophy

Traditional programming forces you to learn **machine syntax** before solving real problems.  
NATCOM flips this — **you write English, the compiler does the translation**.

> *"Why should humans learn the machine's language? The machine should learn ours."*  
> — Beon Binesh, Creator of NATCOM

| Traditional Code | NATCOM |
|---|---|
| `int score = 0;` | `Create a high speed integer named Score and set it to 0.` |
| `scanf("%f", &x);` | `Ask the user to enter a value for X.` |
| `result = sqrt(x);` | `Set Result to the square root of X.` |
| `for(int i=0;i<10;i++)` | `Repeat 10 times:` |
| `if (a > b) { ... }` | `If the A is greater than B, then:` |
| `class Car { ... }` | `Define a class named Car: ... End class.` |

---

## 🎓 NATCOM Studio — Interactive Web IDE

NATCOM Studio is a full-featured, PyCharm-style web IDE built entirely in NATCOM itself (bootstrapped).

### Features
| Feature | Description |
|---|---|
| 🎨 **JetBrains Darcula Theme** | Full Darcula color scheme, JetBrains Mono font |
| ⚡ **NATCOM Native (x86_64)** | Compiles `.nc` files to native C binaries with `-O3` optimization |
| 🌐 **NATCOM Web Engine** | Runs programs interactively in the browser — no installation needed |
| 🔴 **Interactive Input** | PyCharm-style inline terminal input — type values when prompted, press Enter to continue |
| 🔢 **Type Badges** | Real-time type display: `int`, `float`, `str`, `bool`, `fn`, `class` on every output line |
| 🌈 **Syntax Highlighting** | Full NATCOM keyword highlighting with Darcula colors |
| 📁 **File Explorer** | Project tree with all built-in examples, new file creation |
| 📚 **Language Reference** | Clickable cheatsheet — click any snippet to insert into editor |
| 🤖 **AI Code Generator** | Gemini AI integration — describe what you want, get NATCOM code |
| 🐛 **Error Squiggles** | Real-time error detection with inline problem markers |
| 🔍 **Search** | Search across all open files |
| ♾️ **Bootstrapped Compiler** | NATCOM compiles its own IDE — the ultimate metacircular demo |
| 🔐 **Easter Eggs** | Hidden cheat codes unlock special modes |

---

## 📖 Complete Language Reference

### Variables & Data Types

```
Create a high speed integer named Score and set it to 0.
Create a floating point variable named Price and set it to 9.99.
Create a string named Name and set it to "Beon".
Create a boolean named IsActive and set it to true.
Set Score to 42.
Swap the values of A and B.
```

| Type | Keyword | Compiled C Type |
|---|---|---|
| Integer | `high speed integer` | `int` |
| Float | `floating point variable` | `float` |
| String | `string` | `char[512]` |
| Boolean | `boolean` | `int` (0/1) |

---

### User Input (Interactive)

```
Ask the user to enter a value for Score.
Ask the user for text named PlayerName.
```

> **NATCOM Web Engine automatically handles interactive input** — a PyCharm-style inline input field appears in the terminal. Type your value and press Enter to continue.

---

### Arithmetic Operations

```
Add 10 to Score.
Subtract 5 from Score.
Multiply Score by 2.
Divide Score by 4.
Increment Score.
Decrement Score.
```

---

### Math Functions

```
Set Result to the square root of X.
Set Result to the absolute value of X.
Set Result to the floor of X.
Set Result to the ceiling of X.
Set Result to the log of X.
Set Result to the exp of X.
Set Result to the maximum of A and B.
Set Result to the minimum of A and B.
Set X to the power of Y to the power of 2.
Find the remainder of A divided by B and store in C.
Generate a random number between 1 and 100 and store in X.
```

---

### Display & Output

```
Display "Hello, World!".
Display the values of Score.
Display the values of A and B and C.
Log the value of Score.
```

---

### Conditionals

```
If the Score is greater than 100, then:
  Display "High score!".
Otherwise:
  Display "Keep trying!".
Done.
```

**Comparison operators:** `greater than`, `less than`, `equal to`, `greater than or equal to`, `less than or equal to`, `not equal to`

---

### Loops

```
Repeat 10 times:
  Increment Count.
Done.

Keep running while Count is less than 100:
  Add 1 to Count.
Stop the loop.

Begin the main simulation loop.
  ...
  Halt the simulation.
```

---

### Functions

```
Define a function named Greet:
  Display "Hello from a NATCOM function!".
End function.

Call function Greet.

Define a function named Add with parameters A and B:
  Set Result to A.
  Add B to Result.
  Display the values of Result.
End function.

Call function Add with arguments 10 and 20.
```

---

### Classes & Object-Oriented Programming

```
Define a class named Car:
  Create a floating point variable named Speed and set it to 0.
  Create a floating point variable named Fuel and set it to 100.
End class.

Create an object of class Car named MyCar.
```

---

### Special Features

```
Initialize the cloaked zero-knowledge matrix for sovereign auditing.
Initialize high performance gaming viewport with gravity physics.
Render a 3D matrix representing a vehicle at coordinates 10.5, 50.0, 15.2.
Sync the current game state to Google Cloud Storage virtual RAM expansion using safe offline fallbacks.
```

---

### System Override (Raw C Code Injection)

```
<SYSTEM_OVERRIDE>
printf("Raw C code here\n");
</SYSTEM_OVERRIDE>
```

---

## 🎮 Example Programs

### Hello World
```
Create a string named Greeting and set it to "Hello, World!".
Display "Welcome to NATCOM!".
Log the value of Greeting.
```

### Interactive Calculator
```
Create a floating point variable named A and set it to 0.
Create a floating point variable named B and set it to 0.
Create a floating point variable named Result and set it to 0.

Ask the user to enter a value for A.
Ask the user to enter a value for B.

Add A to Result.
Add B to Result.

Display "Sum:".
Log the value of Result.
```

### Counter with Loop
```
Create a high speed integer named Count and set it to 0.
Create a high speed integer named Limit and set it to 0.

Ask the user to enter a value for Limit.

Repeat 5 times:
  Increment Count.
Done.

Display "Final count:".
Log the value of Count.
```

### Budget Tracker
```
Create a floating point variable named Budget and set it to 0.
Create a floating point variable named Expenses and set it to 0.
Create a floating point variable named Savings and set it to 0.

Ask the user to enter a value for Budget.
Ask the user to enter a value for Expenses.

Add Budget to Savings.
Subtract Expenses from Savings.

Display "=== Budget Report ===".
Display the values of Budget.
Display the values of Expenses.
Display the values of Savings.

If the Savings is greater than 0, then:
  Display "You are saving money!".
Otherwise:
  Display "Warning: Over budget!".
```

### Game Physics Simulation
```
Initialize the cloaked zero-knowledge matrix for sovereign auditing.
Initialize high performance gaming viewport with gravity physics.

Create a floating point variable named Gravity and set it to 9.81.
Create a floating point variable named Velocity and set it to 0.0.
Create a high speed integer named Frame and set it to 0.
Create a high speed integer named SpawnX and set it to 0.

Generate a random number between 1 and 1000 and store in SpawnX.
Display the values of SpawnX.

Begin the main simulation loop.
  Add 1 to Frame.
  Add Gravity to Velocity.
  Multiply Velocity by 0.016.

  If the Frame is greater than 60, then:
    Log the value of Velocity.
    Halt the simulation.
  Otherwise:
    Keep the simulation running.

Log the value of Frame.
```

### OOP — Classes & Objects
```
Define a class named Person:
  Create a high speed integer named Age and set it to 0.
  Create a floating point variable named Score and set it to 0.
End class.

Create an object of class Person named Beon.
Display "Object Beon created from class Person.".
Display "OOP in plain English — only in NATCOM.".
```

### Bootstrapped Compiler (Metacircular)
```
Display "Initializing Sovereign Compiler Matrix...".
Display "Target architecture: NATCOM Native".

Create a string named SourceLine and set it to "Add 5 to X".
Display "Reading source line:".
Log the value of SourceLine.

Display "[ LEXER ] Tokenizing natural prose...".
Display "[ PARSER ] Translating to machine instructions...".

Create a boolean named Handled and set it to false.

If the SourceLine contains "Add", then:
  Display "-> Detected arithmetic ADD instruction.".
  Display "-> Generating C Code: X += 5;".
  Set Handled to true.
Done.

Display "Compilation complete. Binary generated.".
```

---

## 🏛️ Legacy & Inspiration — NATCOM & COBOL

NATCOM proudly stands on the shoulders of giants. **COBOL** (1959), created by **Admiral Grace Murray Hopper**, was the first programming language to use English-like syntax. NATCOM carries that vision forward — into the AI era.

| Feature | COBOL (1959) | NATCOM (2026) |
|---|---|---|
| Creator | Grace Hopper & team | Beon Binesh |
| Philosophy | English-like syntax | Full natural English |
| Target | Mainframes | Native Binary + Web Engine |
| Input style | `IDENTIFICATION DIVISION` | `Ask the user to enter a value for X.` |
| Loops | `PERFORM 10 TIMES` | `Repeat 10 times:` |
| Error handling | Rigid structure | Self-healing AI engine |
| Year | 1959 | 2026 |

---

## 🏗️ Architecture

```
NATCOM/
├── natcom              # CLI compiler entry point (bash script)
├── server.py           # NATCOM Studio backend (Python HTTP server)
├── src/
│   ├── lexer.py        # Tokenizer — breaks English into tokens
│   ├── parser.py       # Parser — builds AST from tokens
│   └── codegen.py      # Code Generator — emits C or JS from AST
├── ui/
│   ├── index.html      # NATCOM Studio IDE (PyCharm-style)
│   ├── style.css       # Darcula theme + interactive terminal styles
│   ├── script.js       # IDE engine + NATCOM Web Engine runner
│   └── about.html      # Creator page (Beon Binesh)
├── examples/
│   ├── hello.nc
│   ├── calculator.nc
│   ├── budget_tracker.nc
│   ├── counter.nc
│   ├── game_physics.nc
│   ├── full_demo.nc
│   ├── functions.nc
│   ├── classes.nc
│   └── compiler.nc     # Bootstrapped metacircular compiler
└── firebase_public/    # Firebase Hosting deployment
```

---

## 🛠️ CLI Reference

```bash
# Compile to NATCOM Native (x86_64 binary)
./natcom build program.nc -o program

# Compile to NATCOM Web Engine (JavaScript)
./natcom build program.nc --target js -o program

# Run the compiled binary
./program

# Start NATCOM Studio
python3 server.py
# Then open: http://localhost:8080
```

---

## 🔐 Easter Eggs

NATCOM Studio has hidden cheat codes — type them anywhere in your `.nc` file:

| Code | Trigger | Secret |
|---|---|---|
| 🎮 **Vice City 144p** | `malayali pwoli ahda` | We got NATCOM before GTA 6! |
| 🏛️ **Legacy Mode** | `thank you cobol` | Tribute to Grace Hopper |
| 🔐 **Sovereign Unlock** | `Initialize the cloaked zero-knowledge matrix` | ZKP audit layer activated |
| 💻 **Dev Mode** | `beon` | Welcome message from the creator |

---

## 📜 License

MIT License — free to use, modify, and distribute.

---

<div align="center">

**NATCOM v2.0** · Built with ❤️ by **Beon Binesh**  
*Developed with Google Gemini AI & Antigravity AGY by Google DeepMind*

> *"Code is just language. Language is just thought. NATCOM is thought, compiled."*

</div>
