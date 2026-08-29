#include <iostream>
#include <string>

#include "core/EulerIntegrator.h"
#include "core/RK4Integrator.h"

#include "simulations/Projectile/ProjectileSimulation.h"
#include "simulations/DampedOscillator/DampedOscillatorSimulation.h"
#include "simulations/CircularMotion/CircularMotionSimulation.h"
#include "simulations/Circuit/RCCircuitSimulation.h"

int main()
{
    std::cout << "=== Physics Simulator ===\n\n";

    std::cout << "Select Simulation\n";
    std::cout << "1. Projectile Motion\n";
    std::cout << "2. Damped Harmonic Oscillator\n";
    std::cout << "3. Circular Motion\n";
    std::cout << "4. RC Circuit\n";
    std::cout << "Choice: ";

    int simulationChoice;
    std::cin >> simulationChoice;

    std::cout << "\nSelect Integrator\n";
    std::cout << "1. Euler\n";
    std::cout << "2. RK4\n";
    std::cout << "Choice: ";

    int integratorChoice;
    std::cin >> integratorChoice;

    EulerIntegrator euler;
    RK4Integrator rk4;

    const Integrator* integrator = nullptr;

    if (integratorChoice == 1)
    {
        integrator = &euler;
    }
    else if (integratorChoice == 2)
    {
        integrator = &rk4;
    }
    else
    {
        std::cerr << "Invalid integrator choice.\n";
        return 1;
    }

    double dt;
    double endTime;
    std::string filename;

    if (simulationChoice == 1)
    {
        double x0;
        double y0;
        double v0;
        double angle;
        double g;

        std::cout << "\n=== Projectile Motion ===\n";

        std::cout << "Initial x: ";
        std::cin >> x0;

        std::cout << "Initial y: ";
        std::cin >> y0;

        std::cout << "Initial speed: ";
        std::cin >> v0;

        std::cout << "Launch angle (degrees): ";
        std::cin >> angle;

        std::cout << "Gravity: ";
        std::cin >> g;

        std::cout << "Time step dt: ";
        std::cin >> dt;

        std::cout << "End time: ";
        std::cin >> endTime;

        std::cout << "Output filename: ";
        std::cin >> filename;

        if (dt <= 0.0 || endTime <= 0.0)
        {
            std::cerr << "dt and end time must be positive.\n";
            return 1;
        }

        ProjectileSimulation simulation(
            x0,
            y0,
            v0,
            angle,
            g,
            dt,
            endTime,
            *integrator,
            filename
        );

        std::cout << "\nRunning simulation...\n";
        simulation.run();
    }
    else if (simulationChoice == 2)
    {
        double x0;
        double v0;
        double m;
        double k;
        double b;

        std::cout << "\n=== Damped Harmonic Oscillator ===\n";

        std::cout << "Initial position: ";
        std::cin >> x0;

        std::cout << "Initial velocity: ";
        std::cin >> v0;

        std::cout << "Mass: ";
        std::cin >> m;

        std::cout << "Spring constant k: ";
        std::cin >> k;

        std::cout << "Damping coefficient b: ";
        std::cin >> b;

        std::cout << "Time step dt: ";
        std::cin >> dt;

        std::cout << "End time: ";
        std::cin >> endTime;

        std::cout << "Output filename: ";
        std::cin >> filename;

        if (m <= 0.0)
        {
            std::cerr << "Mass must be positive.\n";
            return 1;
        }

        if (dt <= 0.0 || endTime <= 0.0)
        {
            std::cerr << "dt and end time must be positive.\n";
            return 1;
        }

        DampedOscillatorSimulation simulation(
            x0,
            v0,
            m,
            k,
            b,
            dt,
            endTime,
            *integrator,
            filename
        );

        std::cout << "\nRunning simulation...\n";
        simulation.run();
    }
    else if (simulationChoice == 3)
    {
        double x0;
        double y0;
        double vx0;
        double vy0;
        double mass;

        std::cout << "\n=== Circular Motion ===\n";

        std::cout << "Initial x: ";
        std::cin >> x0;

        std::cout << "Initial y: ";
        std::cin >> y0;

        std::cout << "Initial vx: ";
        std::cin >> vx0;

        std::cout << "Initial vy: ";
        std::cin >> vy0;

        std::cout << "Mass: ";
        std::cin >> mass;

        std::cout << "Time step dt: ";
        std::cin >> dt;

        std::cout << "End time: ";
        std::cin >> endTime;

        std::cout << "Output filename: ";
        std::cin >> filename;

        if (mass <= 0.0)
        {
            std::cerr << "Mass must be positive.\n";
            return 1;
        }

        if (x0 * x0 + y0 * y0 == 0.0)
        {
            std::cerr << "Initial radius must be non-zero.\n";
            return 1;
        }

        if (dt <= 0.0 || endTime <= 0.0)
        {
            std::cerr << "dt and end time must be positive.\n";
            return 1;
        }

        CircularMotionSimulation simulation(
            x0,
            y0,
            vx0,
            vy0,
            mass,
            dt,
            endTime,
            *integrator,
            filename
        );

        std::cout << "\nRunning simulation...\n";
        simulation.run();
    }
    else if (simulationChoice == 4)
    {
        double V0;
        double R;
        double C;

        std::cout << "\n=== RC Circuit ===\n";

        std::cout << "Initial voltage: ";
        std::cin >> V0;

        std::cout << "Resistance R: ";
        std::cin >> R;

        std::cout << "Capacitance C: ";
        std::cin >> C;

        std::cout << "Time step dt: ";
        std::cin >> dt;

        std::cout << "End time: ";
        std::cin >> endTime;

        std::cout << "Output filename: ";
        std::cin >> filename;

        if (R <= 0.0 || C <= 0.0)
        {
            std::cerr << "R and C must be positive.\n";
            return 1;
        }

        if (dt <= 0.0 || endTime <= 0.0)
        {
            std::cerr << "dt and end time must be positive.\n";
            return 1;
        }

        RCCircuitSimulation simulation(
            V0,
            R,
            C,
            dt,
            endTime,
            *integrator,
            filename
        );

        std::cout << "\nRunning simulation...\n";
        simulation.run();
    }
    else
    {
        std::cerr << "Invalid simulation choice.\n";
        return 1;
    }

    std::cout << "Simulation complete.\n";
    std::cout << "Results saved to: " << filename << '\n';

    return 0;
}