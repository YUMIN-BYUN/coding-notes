### Project 2 — C++ Extensible Physics Simulator

**Status:** v0.1 Complete

An extensible C++ framework for simulating physical systems using interchangeable numerical integration methods.

The project separates physical system definitions from numerical integration. Each system defines its state and differential equations, while generic integrators advance the state without knowing the physical meaning or dimension of the system.

The simulator provides a CLI for selecting a physical system, choosing an integration method, entering simulation parameters, and exporting the results to CSV.

#### Architecture

The core simulation workflow is:

```text
Physical System
      ↓
derivative(t, state)
      ↓
Numerical Integrator
      ↓
Simulation Loop
      ↓
CSV Output
```

Physical states are represented generically using:

```cpp
using State = std::vector<double>;
```

Numerical integrators operate only on the state and derivative function. This allows the same integration code to simulate systems with different state dimensions and physical meanings.

#### Supported Numerical Integrators

- Explicit Euler Method
- Fourth-order Runge-Kutta Method (RK4)

Both integrators implement a common `Integrator` interface and can be selected at runtime.

#### Supported Physical Systems

**Projectile Motion**

State:

```text
{x, y, vx, vy}
```

Simulates two-dimensional projectile motion under constant gravitational acceleration.

**Damped Harmonic Oscillator**

State:

```text
{x, v}
```

Simulates a damped mass-spring system and records position, velocity, acceleration, kinetic energy, potential energy, and total energy.

**Circular Motion**

State:

```text
{x, y, vx, vy}
```

Simulates uniform circular motion using centripetal acceleration and records orbital radius and kinetic energy.

**RC Circuit**

State:

```text
{V}
```

Simulates capacitor discharge governed by:

```text
dV/dt = -V / (RC)
```

The one-dimensional RC state demonstrates that the framework is not limited to mechanical systems and can be used for general ordinary differential equations.

#### Project Structure

```text
project2/

├── main.cpp
│
├── core/
│   ├── Simulation.h
│   ├── Simulation.cpp
│   ├── CSVWriter.h
│   ├── CSVWriter.cpp
│   ├── State.h
│   ├── Integrator.h
│   ├── EulerIntegrator.h
│   ├── EulerIntegrator.cpp
│   ├── RK4Integrator.h
│   └── RK4Integrator.cpp
│
└── simulations/
    ├── Projectile/
    │   ├── ProjectileSimulation.h
    │   └── ProjectileSimulation.cpp
    │
    ├── DampedOscillator/
    │   ├── DampedOscillatorSimulation.h
    │   └── DampedOscillatorSimulation.cpp
    │
    ├── CircularMotion/
    │   ├── CircularMotionSimulation.h
    │   └── CircularMotionSimulation.cpp
    │
    └── Circuit/
        ├── RCCircuitSimulation.h
        ├── RCCircuitSimulation.cpp
        └── results/
```

The architecture separates the numerical method from the physical model:

```text
Simulation
    ↓
Physical System → derivative(t, state)
    ↓
Integrator
 ┌───────┴───────┐
Euler            RK4
    ↓
Updated State
    ↓
CSVWriter
```

As a result, new physical systems can reuse the existing simulation and integration infrastructure.

#### Development Progress

- [x] Day 1 — Core Simulation Framework & CSV Output
- [x] Day 2 — Projectile Motion & Damped Harmonic Oscillator
- [x] Day 3 — Generic State & Integrator Architecture
- [x] Day 4 — Euler / RK4 Integration & Projectile Validation
- [x] Day 5 — Circular Motion & Integrator Validation
- [x] Day 6 — RC Circuit & Project 1 Integration
- [x] Day 7 — CLI Integration, Final Validation & Project Cleanup

#### Numerical Validation

The numerical simulations were compared against analytical solutions.

Validation included:

- Projectile trajectory
- Damped oscillator position and velocity
- Damped oscillator energy
- Circular orbit and radius conservation
- RC exponential discharge

The Explicit Euler method exhibits the expected first-order numerical error. In circular motion, Euler integration also produces visible outward orbital and energy drift.

RK4 provides significantly higher accuracy and closely reproduces the analytical solutions for the tested time steps.

#### Project 1 Integration

Project 2 was also tested together with the Python Experimental Data Fitting & Analysis Tool from Project 1.

The RK4 RC-circuit simulation generated voltage data for:

```text
V0 = 5 V
R = 1000 Ω
C = 0.001 F
```

giving the theoretical time constant:

```text
τ = RC = 1 s
```

The generated CSV was loaded into Project 1 and fitted using:

```text
V(t) = A exp(Bt) + C
```

The fit recovered approximately:

```text
A ≈ 5
B ≈ -1
C ≈ 0
```

Since:

```text
B = -1 / τ
```

the fitted value gives:

```text
τ ≈ 1 s
```

in agreement with the simulation parameter `RC = 1 s`.

This validates the complete workflow:

```text
C++ Physics Simulation
        ↓
Numerical Integration
        ↓
CSV
        ↓
Python Data Analysis
        ↓
Nonlinear Least Squares
        ↓
Physical Parameter Recovery
```

The fitting results and plots are preserved in:

```text
simulations/Circuit/results/
```

#### Build

The simulator can be compiled with:

```bash
g++ main.cpp core/Simulation.cpp core/CSVWriter.cpp core/EulerIntegrator.cpp core/RK4Integrator.cpp simulations/Projectile/ProjectileSimulation.cpp simulations/DampedOscillator/DampedOscillatorSimulation.cpp simulations/CircularMotion/CircularMotionSimulation.cpp simulations/Circuit/RCCircuitSimulation.cpp -o simulator
```

Run the executable and select:

```text
=== Physics Simulator ===

Select Simulation
1. Projectile Motion
2. Damped Harmonic Oscillator
3. Circular Motion
4. RC Circuit

Select Integrator
1. Euler
2. RK4
```

Simulation parameters and the output filename are then entered through the CLI.

#### v0.1 Scope

Implemented:

- Generic state representation
- Extensible physical-system architecture
- Common numerical integrator interface
- Explicit Euler integration
- Fourth-order Runge-Kutta integration
- Four physical systems
- Analytical-solution validation
- Energy and numerical-error tracking where applicable
- CSV result export
- Runtime simulation and integrator selection
- Integration with Project 1

Not included in v0.1:

- Event detection
- Ground-collision termination
- Adaptive time stepping
- Additional numerical integrators
- LC / RLC circuits
- Root finding
- CMake build configuration
- GUI