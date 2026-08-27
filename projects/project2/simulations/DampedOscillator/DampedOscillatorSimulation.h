#ifndef DAMPEDOSCILLATORSIMULATION_H
#define DAMPEDOSCILLATORSIMULATION_H

#include <string>
#include "../../core/Simulation.h"
#include "../../core/CSVWriter.h"
#include "../../core/State.h"
#include "../../core/Integrator.h"

class DampedOscillatorSimulation : public Simulation
{
private:
    State state;    

    //parameters
    double m;
    double k;
    double b;
    
    //initial state
    double initialX;
    double initialV;

    const Integrator& integrator;

    CSVWriter writer;

    State derivative(double time, const State& state) const;

public:
    DampedOscillatorSimulation(
        double x0,
        double v0,
        double m,
        double k,
        double b,
        double dt,
        double endTime,
        const Integrator& integrator,
        const std::string& filename
    );

    void step() override;
    void record() override;
};

#endif