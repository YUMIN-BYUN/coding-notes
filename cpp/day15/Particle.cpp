#include <iostream>
#include "Particle.h"

using namespace std;


Particle::Particle(double mass,double x,double y,double vx,double vy)
{
    this->mass = mass;
    this->x = x;
    this->y =  y;
    this->vx = vx;
    this->vy = vy;
}

void Particle::showInfo() const
{
    cout << "Mass: " << mass << endl;
    cout << "Position: (" << x << ", " << y << ")" << endl;
    cout << "Velocity: (" << vx << ", " << vy << ")" << endl; 
}
