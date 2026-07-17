// functions.nc — Functions in NATCOM
// Demonstrates defining and calling custom functions.

// ─── Define a greeting function ───────────────────────────────────────
Define a function named Greet:
  Display "Hello from inside a function!".
  Display "Functions help you reuse code.".
End function.

// ─── Define a math helper function ─────────────────────────────────────
Define a function named DoubleIt with arguments Number:
  Multiply Number by 2.
  Log the value of Number.
End function.

// ─── Main program ──────────────────────────────────────────────────────
Display "=== NATCOM Function Demo ===".
Print a blank line.

// Call the greeting function
Call function Greet.

Print a blank line.

// Create a value and call the math function
Create a floating point variable named Value and set it to 7.
Display "Original value:".
Log the value of Value.

Call function DoubleIt with arguments Value.

Print a blank line.
Display "Function demo complete!".
