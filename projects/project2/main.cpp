#include "simulations/DampedOscillator/DampedOscillatorSimulation.h"

int main()
{
    DampedOscillatorSimulation simulation(
        1.0,
        0.0,
        1.0,
        4.0,
        0.4,
        0.01,
        15.0,
        "damped_oscillator.csv"
    );

    simulation.run();

    return 0;
}