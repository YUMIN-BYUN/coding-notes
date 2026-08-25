#include "Simulation.h"

Simulation::Simulation(double dt, double endTime)
    : time(0.0), dt(dt), endTime(endTime)
{
}

void Simulation::run()
{
    while (time < endTime)
    {
        record();
        step();
        time += dt;
    }
}