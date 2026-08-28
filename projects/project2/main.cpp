#include "core/EulerIntegrator.h"
#include "core/RK4Integrator.h"
#include "simulations/CircularMotion/CircularMotionSimulation.h"

int main()
{
    EulerIntegrator euler;
    RK4Integrator rk4;

    double x0 = 2.0;
    double y0 = 0.0;
    double vx0 = 0.0;
    double vy0 = 3.0;

    double mass = 1.0;
    double dt = 0.01;
    double endTime = 10.0;

    CircularMotionSimulation eulerSimulation(
        x0,
        y0,
        vx0,
        vy0,
        mass,
        dt,
        endTime,
        euler,
        "circular_euler.csv"
    );

    CircularMotionSimulation rk4Simulation(
        x0,
        y0,
        vx0,
        vy0,
        mass,
        dt,
        endTime,
        rk4,
        "circular_rk4.csv"
    );

    eulerSimulation.run();
    rk4Simulation.run();

    return 0;
}