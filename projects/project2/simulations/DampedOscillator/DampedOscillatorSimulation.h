#ifndef DAMPEDOSCILLATORSIMULATION_H
#define DAMPEDOSCILLATORSIMULATION_H

#include <string>
#include "../../core/Simulation.h"
#include "../../core/CSVWriter.h"

class DampedOscillatorSimulation : public Simulation
{
private:
    //current state
    double x;
    double v;

    //parameters
    double m;
    double k;
    double b;

    //initial state
    double initialX;
    double initialV;

    CSVWriter writer;

public:
    DampedOscillatorSimulation(
        double x0,
        double v0,
        double m,
        double k,
        double b,
        double dt,
        double endTime,
        const std::string& filename
    );

    void step() override;
    void record() override;
};

#endif