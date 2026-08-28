#include "CircularMotionSimulation.h"
#include <cmath>

CircularMotionSimulation::CircularMotionSimulation(
    double x0,
    double y0,
    double vx0,
    double vy0,
    double mass,
    double dt,
    double endTime,
    const Integrator& integrator,
    const std::string& filename
)
    : Simulation(dt, endTime),
      state{x0, y0, vx0, vy0},
      mass(mass),
      omega((x0 * vy0 - y0 * vx0) / (x0 * x0 + y0 * y0)),
      initialRadius(std::sqrt(x0 * x0 + y0 * y0)),
      phi(std::atan2(y0, x0)),
      integrator(integrator),
      writer(filename)
{
    writer.writeHeader(
        "Time,X,Y,Vx,Vy,Ax,Ay,Radius,"
        "KineticEnergy,"
        "XExact,YExact,VxExact,VyExact,AxExact,AyExact,RadiusExact,"
        "KineticEnergyExact,"
        "XError,YError,VxError,VyError,AxError,AyError,"
        "KineticEnergyError,RadiusError"
    );
}

State CircularMotionSimulation::derivative(
    double time,
    const State& state
) const
{
    double x  = state[0];
    double y  = state[1];
    double vx = state[2];
    double vy = state[3];

    double dxdt  = vx;
    double dydt  = vy;
    double dvxdt = -omega * omega * x;
    double dvydt = -omega * omega * y;

    return {dxdt, dydt, dvxdt, dvydt};
}

void CircularMotionSimulation::step()
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

void CircularMotionSimulation::record()
{
    // Numerical state
    double x  = state[0];
    double y  = state[1];
    double vx = state[2];
    double vy = state[3];

    double radius = std::sqrt(x * x + y * y);

    double ax = -omega * omega * x;
    double ay = -omega * omega * y;

    double kineticEnergy =
        0.5 * mass * (vx * vx + vy * vy);

    // Exact solution
    double angle = omega * time + phi;

    double xExact  = initialRadius * std::cos(angle);
    double yExact  = initialRadius * std::sin(angle);

    double vxExact = -initialRadius * omega * std::sin(angle);
    double vyExact =  initialRadius * omega * std::cos(angle);

    double axExact =
        -initialRadius * omega * omega * std::cos(angle);

    double ayExact =
        -initialRadius * omega * omega * std::sin(angle);

    double kineticEnergyExact =
        0.5 * mass * (vxExact * vxExact + vyExact * vyExact);

    // Errors
    double xError  = x  - xExact;
    double yError  = y  - yExact;
    double vxError = vx - vxExact;
    double vyError = vy - vyExact;

    double axError = ax - axExact;
    double ayError = ay - ayExact;

    double kineticEnergyError =
        kineticEnergy - kineticEnergyExact;

    double radiusError =
        radius - initialRadius;

    // CSV output
    std::string row =
        std::to_string(time) + "," +
        std::to_string(x) + "," +
        std::to_string(y) + "," +
        std::to_string(vx) + "," +
        std::to_string(vy) + "," +
        std::to_string(ax) + "," +
        std::to_string(ay) + "," +
        std::to_string(radius) + "," +
        std::to_string(kineticEnergy) + "," +
        std::to_string(xExact) + "," +
        std::to_string(yExact) + "," +
        std::to_string(vxExact) + "," +
        std::to_string(vyExact) + "," +
        std::to_string(axExact) + "," +
        std::to_string(ayExact) + "," +
        std::to_string(initialRadius) + "," +
        std::to_string(kineticEnergyExact) + "," +
        std::to_string(xError) + "," +
        std::to_string(yError) + "," +
        std::to_string(vxError) + "," +
        std::to_string(vyError) + "," +
        std::to_string(axError) + "," +
        std::to_string(ayError) + "," +
        std::to_string(kineticEnergyError) + "," +
        std::to_string(radiusError);

    writer.writeRow(row);
}