#ifndef RCCIRCUITSIMULATION_H
#define RCCIRCUITSIMULATION_H

#include <string>
#include "../../core/Simulation.h"
#include "../../core/CSVWriter.h"
#include "../../core/State.h"
#include "../../core/Integrator.h"

class RCCircuitSimulation : public Simulation
{
private:
    State state;    

    //parameters
    double R;
    double C;
    double initialV;
    
    const Integrator& integrator;

    CSVWriter writer;

    State derivative(double time, const State& state) const;

public:
    RCCircuitSimulation(
        double V0,
        double R,
        double C,
        double dt,
        double endTime,
        const Integrator& integrator,
        const std::string& filename
    );

    void step() override;
    void record() override;
};

#endif