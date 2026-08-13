#ifndef PARTICLE_H
#define PARTICLE_H

class Particle
{
public:
    double mass;
    double x;
    double y;
    double vx;
    double vy;

    Particle(double mass,double x,double y,double vx,double vy);

    void showInfo() const;
    
};


#endif