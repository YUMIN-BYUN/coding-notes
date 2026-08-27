#ifndef PROJECTILESIMULATION_H
#define PROJECTILESIMULATION_H

#include <string>

#include "../../core/Simulation.h"
#include "../../core/CSVWriter.h"
#include "../../core/State.h"
#include "../../core/Integrator.h"

class ProjectileSimulation : public Simulation
{
private:
    State state;

    double g;

    //initial state
    double initialX;
    double initialY;
    double initialVx;
    double initialVy;

    const Integrator& integrator;

    CSVWriter writer;

    State derivative(double time, const State& state) const;

public:
    ProjectileSimulation(
        double x0,
        double y0,
        double v0,
        double angleDeg,
        double g,
        double dt,
        double endTime,
        const Integrator& integrator,
        const std::string& filename
    );

    void step() override;
    void record() override;

};


#endif