#include "simulations/DummySimulation.h"

int main()
{
    DummySimulation simulation(1.0, 5.0);

    simulation.run();

    return 0;
}