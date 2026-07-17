// ╔══════════════════════════════════════════════════════════════════╗
// ║           budget_tracker.nc — Monthly Budget Tracker             ║
// ║           NATCOM Example: User Input + Conditionals              ║
// ╚══════════════════════════════════════════════════════════════════╝

// Step 1: Declare all variables with initial zero values
Create a floating point variable named MonthlyIncome and set it to 0.
Create a floating point variable named Rent and set it to 0.
Create a floating point variable named Food and set it to 0.
Create a floating point variable named Transport and set it to 0.
Create a floating point variable named Entertainment and set it to 0.

// Step 2: Get user inputs
Ask the user to enter a value for MonthlyIncome.
Ask the user to enter a value for Rent.
Ask the user to enter a value for Food.
Ask the user to enter a value for Transport.
Ask the user to enter a value for Entertainment.

// Step 3: Calculate total expenses
Create a floating point variable named TotalExpenses and set it to 0.
Add Rent to TotalExpenses.
Add Food to TotalExpenses.
Add Transport to TotalExpenses.
Add Entertainment to TotalExpenses.

// Step 4: Calculate savings
Create a floating point variable named Savings and set it to 0.
Add MonthlyIncome to Savings.
Subtract TotalExpenses from Savings.

// Step 5: Display the report
Display "=== Monthly Budget Report ==="
Display the values of MonthlyIncome.
Display the values of TotalExpenses.
Display the values of Savings.

// Step 6: Give advice based on savings
If the Savings is greater than 0, then:
  Display "Great! You have savings this month."
Otherwise:
  Display "Warning: You are over budget this month."
