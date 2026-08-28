#include "RCCircuitSimulation.h"
#include <cmath>

RCCircuitSimulation::RCCircuitSimulation(
    double V0,
    double R,
    double C,
    double dt,
    double endTime,
    const Integrator& integrator,
    const std::string& filename
)
    : Simulation(dt, endTime),
    state{V0},
    R(R),
    C(C),
    initialV(V0),
    integrator(integrator),
    writer(filename)
{
    writer.writeHeader(
    "Time,Voltage,VoltageExact,VoltageError"
);
}

State RCCircuitSimulation::derivative(
    double time,
    const State& state
) const
{
    double V = state[0];

    double dVdt = -V/(R*C);

    return {dVdt};
}

void RCCircuitSimulation::step()
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

void RCCircuitSimulation::record()
{
    double V = state[0];
    double tau = R*C;
    double V0 = initialV;

    double VExact = V0 * std::exp(-time/tau);
        
    double VError = V - VExact;

    std::string row =
        std::to_string(time)
        + ","
        + std::to_string(V)
        + ","
        + std::to_string(VExact)
        + ","
        + std::to_string(VError);
        
    writer.writeRow(row);
}

    
