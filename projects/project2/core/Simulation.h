#ifndef SIMULATION_H
#define SIMULATION_H

class Simulation
{
protected:
    double time;
    double dt;
    double endTime;

public:
    Simulation(double dt, double endTime);

    virtual ~Simulation() = default;

    virtual void step() = 0;
    virtual void record() = 0;

    void run();
};

#endif 