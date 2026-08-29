# Coding Notes

A personal repository documenting my study of programming, scientific computing, and computational physics.

## Purpose

This repository contains my learning materials, source code, LaTeX documents, and projects created while studying:

- Python
- C++
- Scientific Computing
- Computational Physics

The notes are written during the learning process and are continuously improved as my understanding grows.

AI is used as a learning assistant for concept explanations, discussions, code review, practice design, software architecture, and document generation. Code and projects are reviewed, tested, and studied as part of the learning process.

## Repository Structure

```text
coding-notes/

├── python/
├── cpp/
└── projects/
```

## Progress

### Python

- [x] Day 1 — Python Fundamentals
- [x] Day 2 — Loops and Functions
- [x] Day 3 — Data Structures
- [x] Day 4 — Modules and File I/O
- [x] Day 5 — OOP Basics
- [x] Day 6 — Inheritance
- [x] Day 7 — NumPy Basics
- [x] Day 8 — Pandas
- [x] Day 9 — Matplotlib
- [x] Day 10 — Python Project Preparation
- [x] Day 11 — Comprehensive Practice
- [x] Day 12 — Stock Portfolio Analyzer

### C++

- [x] Day 1 — C++ Basics
- [x] Day 2 — Control Flow
- [x] Day 3 — Pointers and Arrays
- [x] Day 4 — References and Dynamic Memory
- [x] Day 5 — Struct & Header Files
- [x] Day 6 — Classes
- [x] Day 7 — Deep Copy and RAII
- [x] Day 8 — Inheritance and Polymorphism
- [x] Day 9 — Templates
- [x] Day 10 — STL Basics
- [x] Day 11 — STL Associative Containers
- [x] Day 12 — STL Advanced
- [x] Day 13 — File I/O and Exception Handling
- [x] Day 14 — C++ Integration
- [x] Day 15 — Two-Body Gravity Simulation

## Projects

### Project 1 — Python Experimental Data Fitting & Analysis Tool

**Status:** v0.1 Complete

A scientific data fitting and analysis application designed for experimental physics data.

The program provides a GUI-based workflow for loading experimental datasets, selecting variables and uncertainties, fitting mathematical models, evaluating fit quality, visualizing residuals, and exporting analysis results.

It is designed as a reusable tool for analyzing experimental physics data while also serving as a project for studying numerical fitting methods and scientific Python.

#### Features

**Data Input**

- CSV-based experimental data input
- Interactive x/y column selection
- Optional y-uncertainty selection
- Numeric and finite-value validation
- Positive uncertainty validation

**Fitting Models**

- Linear
- Polynomial with user-defined degree
- Exponential
- Sinusoidal
- Gaussian
- Custom user-defined functions

**Fitting Methods**

- Ordinary Least Squares
- Weighted Least Squares using y-uncertainty
- Nonlinear Least Squares
- Automatic initial guess estimation for supported nonlinear models
- Manual initial guess input

**Statistical Analysis**

- Parameter uncertainty from covariance matrices
- Residual analysis
- RMSE
- R²
- χ²
- Reduced χ²
- Degrees of freedom

**Visualization**

- Raw data preview
- Error bars
- Fitted curves
- Residual plots
- Linear and logarithmic axis scales
- Embedded Matplotlib plots inside the GUI

**Interface**

- Tkinter GUI
- Model-dependent input controls
- Quick Mode for concise results
- Detail Mode for fitting-method and statistical information
- Raw Data / Fit / Residual plot tabs

**Result Export**

- CSV fitting results
- JSON fitting results
- Fit plot PNG
- Residual plot PNG

#### Project Structure

```text
project1/

├── gui.py
├── main.py
├── data/
├── results/
├── src/
│   ├── __init__.py
│   ├── analysis.py
│   ├── data_loader.py
│   ├── fitting.py
│   ├── metrics.py
│   ├── models.py
│   ├── plotting.py
│   ├── result_formatter.py
│   └── result_io.py
└── tests/
```

The project separates the fitting and analysis core from the user interface:

```text
GUI / CLI
    ↓
analysis.py
    ↓
fitting.py + models.py + metrics.py
    ↓
result_formatter.py + plotting.py + result_io.py
```

This allows the numerical analysis code to remain independent of the GUI.

#### Development Progress

- [x] Day 1 — Project Architecture & Experimental Data Input
- [x] Day 2 — Linear & Polynomial Least Squares
- [x] Day 3 — Fit Quality & Residual Analysis
- [x] Day 4 — Nonlinear Least Squares
- [x] Day 5 — Gaussian, Initial Guess & Parameter Uncertainty
- [x] Day 6 — Error Bars, Weighted Least Squares, χ² & Custom Function
- [x] Day 7 — Core Integration, Result Saving, Validation & GUI

#### Validation

The final v0.1 workflow was tested with synthetic datasets for:

- Linear fitting
- Polynomial fitting
- Exponential fitting
- Sinusoidal fitting
- Gaussian fitting
- Custom function fitting
- Weighted fitting with measurement uncertainties
- Parameter recovery
- Fit and residual visualization
- Result export

Input and edge-case validation is also included for invalid uncertainties, mismatched data lengths, invalid polynomial degrees, insufficient data points, NaN/infinite values, and constant-y datasets.

#### v0.1 Scope

Implemented:

- Multiple fitting models
- OLS and WLS
- y-uncertainty
- Parameter uncertainty
- Fit-quality statistics
- Residual analysis
- Automatic/manual initial guesses
- GUI workflow
- Result and plot export

Not included in v0.1:

- x-uncertainty
- Orthogonal Distance Regression (ODR)
- Advanced parameter-correlation analysis
- Production-grade custom expression parsing
- Advanced GUI styling

---

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

---

### Project 3 — Sensor / Tracking Project

**Status:** Planned

A physics-oriented experimental project focused on measurement, motion tracking, or sensor-based data acquisition.

Possible directions include:

- Video-based motion tracking
- Position and trajectory extraction
- Physical scale calibration
- Arduino sensor data acquisition
- Integration with experimental data analysis tools

## Learning Workflow

1. Study programming and scientific computing concepts
2. Understand the mathematical or computational principles
3. Review small examples
4. Implement and test individual features
5. Review code and identify problems
6. Integrate components into larger programs
7. Document important concepts and design decisions
8. Apply the concepts through scientific computing projects

## AI-Assisted Learning

AI tools are used throughout this repository as study assistants.

They are used for:

- explaining unfamiliar concepts
- discussing mathematical and numerical methods
- reviewing and debugging code
- creating practice problems and test cases
- organizing study plans and notes
- assisting with LaTeX documentation
- discussing software architecture and project design
- assisting with repetitive implementation tasks such as GUI construction

The emphasis of this repository is on understanding the underlying concepts, testing implementations, interpreting results, and applying programming to scientific problems.

---

**Last updated: August 2026**