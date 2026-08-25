#ifndef PROJECTILESIMULATION_H
#define PROJECTILESIMULATION_H

#include <string>

#include "../../core/Simulation.h"
#include "../../core/CSVWriter.h"

class ProjectileSimulation : public Simulation
{
private:
    double x;
    double y;
    double vx;
    double vy;
    double g;

    double initialX;
    double initialY;
    double initialVx;
    double initialVy;

    CSVWriter writer;

public:
    ProjectileSimulation(
        double x0,
        double y0,
        double v0,
        double angleDeg,
        double g,
        double dt,
        double endTime,
        const std::string& filename
    );

    void step() override;
    void record() override;

};


#endif