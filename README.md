# Coding Notes

A personal repository documenting my study of programming, scientific computing, and computational physics.

## Purpose

This repository contains my learning materials, source code, LaTeX documents, and projects created while studying:

* Python
* C++
* Arduino
* Scientific Computing
* Computational Physics

The notes are written during the learning process and are continuously improved as my understanding grows.

AI is used as a learning assistant for concept explanations, discussions, code review, practice design, and document generation. All example code and practice problems are reviewed, implemented, tested, and studied by myself.

## Repository Structure

```text
coding-notes/
├── python/
├── cpp/
├── arduino/
└── projects/
```

## Progress

### Python

* [x] Day 1 — Python Fundamentals
* [x] Day 2 — Loops and Functions
* [x] Day 3 — Data Structures
* [x] Day 4 — Modules and File I/O
* [x] Day 5 — OOP Basics
* [x] Day 6 — Inheritance
* [x] Day 7 — NumPy Basics
* [x] Day 8 — Pandas
* [x] Day 9 — Matplotlib
* [x] Day 10 — Python Project Preparation
* [x] Day 11 — Comprehensive Practice
* [x] Day 12 — Stock Portfolio Analyzer

### C++

* [x] Day 1 — C++ Basics
* [x] Day 2 — Control Flow
* [x] Day 3 — Pointers and Arrays
* [x] Day 4 — References and Dynamic Memory
* [x] Day 5 — Struct & Header Files
* [x] Day 6 — Classes
* [x] Day 7 — Deep Copy and RAII
* [x] Day 8 — Inheritance and Polymorphism
* [x] Day 9 — Templates
* [x] Day 10 — STL Basics
* [x] Day 11 — STL Associative Containers
* [x] Day 12 — STL Advanced
* [x] Day 13 — File I/O and Exception Handling
* [x] Day 14 — C++ Integration
* [x] Day 15 — Two-Body Gravity Simulation

## Projects

### Project 1 — Python Experimental Data Fitting & Analysis Tool

**Status:** In Progress

A scientific data analysis tool designed for experimental physics data. The goal is to build a reusable program for loading experimental datasets, fitting mathematical models, evaluating fit quality, handling measurement uncertainty, and exporting analysis results.

#### Planned Features

* CSV-based experimental data input
* Linear fitting
* Polynomial fitting
* Exponential fitting
* Sinusoidal fitting
* Gaussian fitting
* Custom function fitting
* Ordinary Least Squares
* Weighted Least Squares
* y-uncertainty and error bars
* Parameter uncertainty estimation
* R² and RMSE
* Residual analysis
* χ² and reduced χ²
* Quick Mode and Detail Mode
* CSV, JSON, and PNG result export

#### Progress

* [x] Day 1 — Project Architecture & Experimental Data Input
* [ ] Day 2 — Linear & Polynomial Least Squares
* [ ] Day 3 — Fit Quality & Residual Analysis
* [ ] Day 4 — Nonlinear Least Squares
* [ ] Day 5 — Gaussian, Initial Guess & Parameter Uncertainty
* [ ] Day 6 — Error Bars, Weighted Least Squares, χ² & Custom Function
* [ ] Day 7 — Result Saving, Quick/Detail Mode & Full Validation

#### Day 1 Implemented

* Project module structure
* CSV loading with pandas
* Interactive x/y column selection
* Optional y-uncertainty selection
* Conversion to NumPy arrays
* Column validation
* Numeric data validation
* NaN and infinity validation
* Positive uncertainty validation

### Project 2 — C++ Extensible Physics Simulator

**Status:** Planned

An extensible C++ framework for implementing and simulating multiple physical systems.

Initial systems will include:

* Projectile Motion
* Damped Harmonic Oscillator
* Circular / Centripetal Motion
* RC / LC Circuit

The simulator will be designed so that additional physical systems can be added without rebuilding the overall program structure.

### Project 3 — Sensor / Tracking Project

**Status:** Planned

A physics-oriented experimental project focused on measurement, motion tracking, or sensor-based data acquisition.

Possible directions include:

* Video-based motion tracking
* Position and trajectory extraction
* Physical scale calibration
* Arduino sensor data acquisition
* Integration with experimental data analysis tools

## Learning Workflow

1. Study programming and scientific computing concepts
2. Understand the mathematical or computational principles
3. Review small examples
4. Implement features independently
5. Receive code review and corrections
6. Integrate individual components into larger programs
7. Document important concepts when necessary
8. Apply the concepts through scientific computing projects

## AI-Assisted Learning

AI tools are used throughout this repository as study assistants.

They are used for:

* explaining unfamiliar concepts
* discussing mathematical and implementation details
* reviewing code
* creating practice problems
* organizing study plans and notes
* assisting with LaTeX documentation
* discussing software architecture and project design

The code is written and tested during the learning process, and the final understanding and implementation are verified through direct practice.

---

*Last updated: August 2026*
