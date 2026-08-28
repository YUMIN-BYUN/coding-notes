#ifndef CIRCULATMOTIONSIMULATION_H
#define CIRCULATMOTIONSIMULATION_H

#include <string>
#include "../../core/Simulation.h"
#include "../../core/CSVWriter.h"
#include "../../core/State.h"
#include "../../core/Integrator.h"

class CircularMotionSimulation : public Simulation
{
private:
    State state;    

    //parameters
    double mass;
    double omega;
    double initialRadius;
    double phi;
    

    const Integrator& integrator;

    CSVWriter writer;

    State derivative(double time, const State& state) const;

public:
    CircularMotionSimulation(
        double x0,
        double y0,
        double vx0,
        double vy0,
        double mass,
        double dt,
        double endTime,
        const Integrator& integrator,
        const std::string& filename
    );

    void step() override;
    void record() override;
};

#endif