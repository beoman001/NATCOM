// ╔══════════════════════════════════════════════════════════════════╗
// ║           game_physics.nc — Gravity Simulation                   ║
// ║           NATCOM Example: Loops, Math, and Conditions            ║
// ╚══════════════════════════════════════════════════════════════════╝

Create a floating point variable named PlayerY and set it to 100.0.
Create a floating point variable named Velocity and set it to 0.0.
Create a floating point variable named Gravity and set it to 9.8.
Create a high speed integer named Ticks and set it to 0.

Display "=== Dropping object from 100m ==="

Begin the main simulation loop.
  Increment Ticks.
  
  Add Gravity to Velocity.
  Subtract Velocity from PlayerY.
  
  Log the value of PlayerY.

  If the PlayerY is less than 0.0, then:
    Display "IMPACT! Object hit the ground."
    Halt the simulation.
  Otherwise:
    Keep the simulation running.

Display "Total simulation ticks:"
Log the value of Ticks.
