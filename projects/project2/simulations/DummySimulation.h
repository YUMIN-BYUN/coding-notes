#ifndef DUMMY_SIMULATION_H
#define DUMMY_SIMULATION_H

#include "../core/Simulation.h"
#include "../core/CSVWriter.h"

class DummySimulation : public Simulation
{
private:
    double value;
    CSVWriter writer;

public:
    DummySimulation(double dt, double endTime);

    void step() override;
    void record() override;
};

#endif