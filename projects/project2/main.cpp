#include "core/RK4Integrator.h"
#include "simulations/Projectile/ProjectileSimulation.h"

int main()
{
    RK4Integrator rk4;

    ProjectileSimulation simulation(
        0.0,      // x0
        0.0,      // y0
        20.0,     // v0
        45.0,     // angleDeg
        9.81,     // g
        0.01,     // dt
        2.0,      // endTime
        rk4,
        "projectile_rk4.csv"
    );

    simulation.run();

    return 0;
}