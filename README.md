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

**Status:** Planned

An extensible C++ framework for implementing and simulating multiple physical systems.

Initial systems will include:

- Projectile Motion
- Damped Harmonic Oscillator
- Circular / Centripetal Motion
- RC / LC Circuit

The simulator will be designed so that additional physical systems can be added without rebuilding the overall program structure.

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