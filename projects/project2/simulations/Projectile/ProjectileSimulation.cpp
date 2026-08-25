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
    const std::string& filename)
    : Simulation(dt, endTime),
      x(x0),
      y(y0),
      vx(0.0),
      vy(0.0),
      g(g),
      writer(filename)

{
    double angleRad = angleDeg * 3.141592653589793 / 180.0;
    vx = v0 * std::cos(angleRad);
    vy = v0 * std::sin(angleRad);

    initialX = x;
    initialY = y;
    initialVx = vx;
    initialVy = vy;

    writer.writeHeader("Time,X,Y,Vx,Vy,Speed,X_exact,Y_exact,X_error,Y_error");
}

void ProjectileSimulation::step()
{
    x += vx * dt;
    y += vy * dt;
    vy -= g* dt;
}

void ProjectileSimulation::record()
{
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