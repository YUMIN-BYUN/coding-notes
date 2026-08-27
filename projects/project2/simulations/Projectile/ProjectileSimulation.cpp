#include "ProjectileSimulation.h"
#include <cmath>

ProjectileSimulation::ProjectileSimulation(
    double x0,
    double y0,
    double v0,
    double angleDeg,
    double g,
    double dt,
    double endTime,
    const Integrator& integrator,
    const std::string& filename)
    : Simulation(dt, endTime),
      state{x0,y0,0.0,0.0},
      g(g),
      integrator(integrator),
      writer(filename)

{
    double angleRad = angleDeg * 3.141592653589793 / 180.0;
    state[2] = v0 * std::cos(angleRad);
    state[3] = v0 * std::sin(angleRad);

    initialX = state[0];
    initialY = state[1];
    initialVx = state[2];
    initialVy = state[3];

    writer.writeHeader("Time,X,Y,Vx,Vy,Speed,X_exact,Y_exact,X_error,Y_error");
}

State ProjectileSimulation::derivative(
    double time,
    const State& state
) const
{
    double vx = state[2];
    double vy = state[3];

    double dxdt = vx;
    double dydt = vy;
    double dvxdt = 0.0;
    double dvydt = -g;

    return {dxdt, dydt, dvxdt, dvydt};
}

void ProjectileSimulation::step()
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

void ProjectileSimulation::record()
{
    double x = state[0];
    double y = state[1];
    double vx = state[2];
    double vy = state[3];

    double xExact = initialX + initialVx * time;

    double yExact =
        initialY
        + initialVy * time
        - 0.5 * g * time * time;

    double xError = x - xExact;
    double yError = y - yExact;


    double speed = std::sqrt(vx*vx + vy*vy);

    std::string row =
        std::to_string(time)
        + ","
        + std::to_string(x)
        + ","
        + std::to_string(y)
        + ","
        + std::to_string(vx)
        + ","
        + std::to_string(vy)
        + ","
        + std::to_string(speed)
        + ","
        + std::to_string(xExact)
        + ","
        + std::to_string(yExact)
        + ","
        + std::to_string(xError)
        + ","
        + std::to_string(yError);

    writer.writeRow(row);
}