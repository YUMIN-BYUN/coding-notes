#include "Physics.h"
#include <cmath>

Position getRelativePosition(
    const Particle& particle1,
    const Particle& particle2
)
{
    Position relativeposition;
    relativeposition.x = particle2.x - particle1.x;
    relativeposition.y = particle2.y - particle1.y;
    return relativeposition;
}

Accelerations getAccelerations(
    const Particle& particle1,
    const Particle& particle2
)
{
    Position relativeposition = getRelativePosition(particle1,particle2);
    double x = relativeposition.x;
    double y = relativeposition.y;
    double m1 = particle1.mass;
    double m2 = particle2.mass;
    double r = sqrt(x*x + y*y);

    Accelerations accelerations;
    const double G = 6.67430e-11;
    accelerations.acceleration1.ax = G*(m2)*(x)/(r*r*r);
    accelerations.acceleration1.ay = G*(m2)*(y)/(r*r*r);
    accelerations.acceleration2.ax = -G*(m1)*(x)/(r*r*r);
    accelerations.acceleration2.ay = -G*(m1)*(y)/(r*r*r);
    
    return accelerations;
}