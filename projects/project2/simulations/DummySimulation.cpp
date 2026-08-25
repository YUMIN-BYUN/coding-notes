#include "DummySimulation.h"
#include <string>

DummySimulation::DummySimulation(double dt, double endTime)
    : Simulation(dt, endTime),
      value(0.0),
      writer("dummy.csv")
{
    writer.writeHeader("time,value");
}

void DummySimulation::step()
{
    value += 1.0;
}

void DummySimulation::record()
{
    std::string row =
        std::to_string(time)
        + ","
        + std::to_string(value);

    writer.writeRow(row);
}