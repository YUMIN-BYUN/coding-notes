#ifndef PHYSICS_H
#define PHYSICS_H

#include "Particle.h"

struct Position
{
    double x;
    double y;
};

struct Velocity
{
    double vx;
    double vy;
};

struct Acceleration
{
    double ax;
    double ay;
};

struct Accelerations
{
    Acceleration acceleration1;
    Acceleration acceleration2;
};

Position getRelativePosition(
    const Particle& particle1,
    const Particle& particle2
);

Accelerations getAccelerations(
    const Particle& particle1,
    const Particle& particle2
);

#endif