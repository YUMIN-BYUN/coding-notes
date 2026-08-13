#include "Simulation.h"

void step(Particle& particle1, Particle& particle2, double dt)
{
    Accelerations accelerations
    = getAccelerations(particle1,particle2);

    Position oldposition1;
    oldposition1.x = particle1.x;
    oldposition1.y = particle1.y;
    Position oldposition2;
    oldposition2.x = particle2.x;
    oldposition2.y = particle2.y;
    Velocity oldvelocity1;
    oldvelocity1.vx = particle1.vx;
    oldvelocity1.vy = particle1.vy;
    Velocity oldvelocity2;
    oldvelocity2.vx = particle2.vx;
    oldvelocity2.vy = particle2.vy;

    Position newposition1;
    newposition1.x = oldposition1.x + oldvelocity1.vx * dt;
    newposition1.y = oldposition1.y + oldvelocity1.vy * dt;
    Position newposition2;
    newposition2.x = oldposition2.x + oldvelocity2.vx * dt;
    newposition2.y = oldposition2.y + oldvelocity2.vy * dt;
    Velocity newvelocity1;
    newvelocity1.vx = oldvelocity1.vx + accelerations.acceleration1.ax * dt;
    newvelocity1.vy = oldvelocity1.vy + accelerations.acceleration1.ay * dt;
    Velocity newvelocity2;
    newvelocity2.vx = oldvelocity2.vx + accelerations.acceleration2.ax * dt;
    newvelocity2.vy = oldvelocity2.vy + accelerations.acceleration2.ay * dt;
    
    particle1.x = newposition1.x;
    particle1.y = newposition1.y;
    particle1.vx = newvelocity1.vx;
    particle1.vy = newvelocity1.vy;

    particle2.x = newposition2.x;
    particle2.y = newposition2.y;
    particle2.vx = newvelocity2.vx;
    particle2.vy = newvelocity2.vy;
}