#include <iostream>
#include <fstream>
#include "Particle.h"
#include "Physics.h"
#include "Simulation.h"

using namespace std;

int main()
{
    Particle particle1(
        1.989e30,
        0.0, 0.0,
        0.0, 0.0
    );

    Particle particle2(
        5.972e24,
        1.496e11, 0.0,
        0.0, 29780.0
    );

    double dt = 3600.0;
    double totalTime = 365.25 * 24.0 * 3600.0;

    int steps = static_cast<int>(totalTime / dt);

    ofstream file("trajectory.csv");

    if (!file.is_open())
    {
        cout << "Failed to open file" << endl;
        return 1;
    }

    file << "time,x1,y1,x2,y2" << endl;

    for (int i = 0; i <= steps; i++)
    {
        double time = i * dt;

        file << time << ","
             << particle1.x << ","
             << particle1.y << ","
             << particle2.x << ","
             << particle2.y << endl;

        if (i < steps)
        {
            step(particle1, particle2, dt);
        }
    }

    file.close();

    cout << "Simulation completed." << endl;
    cout << "Data saved to trajectory.csv" << endl;

    return 0;
}