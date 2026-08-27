#include "DampedOscillatorSimulation.h"
#include <cmath>

DampedOscillatorSimulation::DampedOscillatorSimulation(
    double x0,
    double v0,
    double m,
    double k,
    double b,
    double dt,
    double endTime,
    const Integrator& integrator,
    const std::string& filename
)
    : Simulation(dt, endTime),
    state{x0, v0},
    m(m),
    k(k),
    b(b),
    initialX(x0),
    initialV(v0),
    integrator(integrator),
    writer(filename)
{
    writer.writeHeader(
    "Time,Position,Velocity,Acceleration,"
    "KineticEnergy,PotentialEnergy,TotalEnergy,"
    "PositionExact,VelocityExact,"
    "KineticEnergyExact,PotentialEnergyExact,TotalEnergyExact,"
    "PositionError,VelocityError,"
    "KineticEnergyError,PotentialEnergyError,TotalEnergyError"
);
}

State DampedOscillatorSimulation::derivative(
    double time,
    const State& state
) const
{
    double x = state[0];
    double v = state[1];

    double dxdt = v;
    double dvdt = -(k/m)*x - (b/m)*v;

    return {dxdt, dvdt};
}

void DampedOscillatorSimulation::step()
{
    state = integrator.step(
        state,
        time,
        dt,
        [this](double t, const State& s)
        {
            return derivative(t, s);
        }
    );
}

void DampedOscillatorSimulation::record()
{
    double x = state[0];
    double v = state[1];

    // analytic validation is only for underdamped case
    double acceleration = -(k/m)*x -(b/m)*v;
    double kineticEnergy = 0.5 * m * v * v;
    double potentialEnergy = 0.5 * k * x * x;
    double totalEnergy = kineticEnergy + potentialEnergy;

    double gamma = b / (2*m);
    double omega_d = sqrt(k/m - gamma*gamma);
    double C1 = initialX;
    double C2 = (initialV+gamma*initialX)/omega_d;

    double xExact =
        exp(-gamma*time)
        * (C1*cos(omega_d*time) + C2*sin(omega_d*time));

    double vExact =
        exp(-gamma*time)
        * (
            (-gamma*C1 + omega_d*C2)*cos(omega_d*time)
            + (-gamma*C2 - omega_d*C1)*sin(omega_d*time)
        );

    double kineticEnergyExact = 0.5 * m * vExact * vExact;
    double potentialEnergyExact = 0.5 * k * xExact * xExact;
    double totalEnergyExact = kineticEnergyExact + potentialEnergyExact;

    double xError = x - xExact;
    double vError = v - vExact;

    double kineticEnergyError = kineticEnergy - kineticEnergyExact;
    double potentialEnergyError = potentialEnergy - potentialEnergyExact;
    double totalEnergyError = totalEnergy - totalEnergyExact;

    std::string row =
        std::to_string(time)
        + ","
        + std::to_string(x)
        + ","
        + std::to_string(v)
        + ","
        + std::to_string(acceleration)
        + ","
        + std::to_string(kineticEnergy)
        + ","
        + std::to_string(potentialEnergy)
        + ","
        + std::to_string(totalEnergy)
        + ","
        + std::to_string(xExact)
        + ","
        + std::to_string(vExact)
        + ","
        + std::to_string(kineticEnergyExact)
        + ","
        + std::to_string(potentialEnergyExact)
        + ","
        + std::to_string(totalEnergyExact)
        + ","
        + std::to_string(xError)
        + ","
        + std::to_string(vError)
        + ","
        + std::to_string(kineticEnergyError)
        + ","
        + std::to_string(potentialEnergyError)
        + ","
        + std::to_string(totalEnergyError);
        
    writer.writeRow(row);
}

    
