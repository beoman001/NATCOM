// NATCOM Self-Hosting Compiler Bootstrapper
// This program simulates compiling the NATCOM compiler using itself.

Display "Initializing NATCOM Bootstrapper...".
Display "Loading NATCOM lexical analyzer...".
Create a string named LexerStatus and set it to "OK".

Display "Loading NATCOM syntax parser...".
Create a string named ParserStatus and set it to "OK".

Display "Loading native code generator...".
Create a string named CodeGenStatus and set it to "OK".

Display "All modules loaded.".

Create a high speed integer named LinesOfCode and set it to 10500.
Create a high speed integer named CompiledLines and set it to 0.

Ask the user for text named TargetFile.
Display "Target file set. Beginning compilation of:".
Log the value of TargetFile.

Display "Compiling...".
Keep running while CompiledLines is less than LinesOfCode:
    Add 1500 to CompiledLines.
    Display "Compiled lines:".
    Log the value of CompiledLines.
Stop the loop.

Display "Linking native binaries...".
Display "NATCOM Compiler Bootstrapped successfully!".
Display "Output written to: natcom_nextgen.exe".
