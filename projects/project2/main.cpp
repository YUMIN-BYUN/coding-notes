#include "simulations/Projectile/ProjectileSimulation.h"

int main()
{
    ProjectileSimulation simulation(
        0,
        0,
        20,
        45,
        9.81,
        0.01,
        3,
        "projectile.csv"
    );

    simulation.run();

    return 0;
}