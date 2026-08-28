#include "core/EulerIntegrator.h"
#include "core/RK4Integrator.h"
#include "simulations/Circuit/RCCircuitSimulation.h"

int main()
{
    EulerIntegrator euler;
    RK4Integrator rk4;

    double V0 = 5.0;
    double R = 1000.0;
    double C = 0.001;
    double dt = 0.01;
    double endTime = 5.0;

    RCCircuitSimulation rcEuler(
        V0,
        R,
        C,
        dt,
        endTime,
        euler,
        "rc_euler.csv"
    );

    rcEuler.run();

    RCCircuitSimulation rcRK4(
        V0,
        R,
        C,
        dt,
        endTime,
        rk4,
        "rc_rk4.csv"
    );

    rcRK4.run();

    return 0;
}