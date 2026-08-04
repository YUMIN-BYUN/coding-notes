#include <iostream>
#include <string>

using namespace std;

class Vehicle
{
public:
    virtual void move() = 0;

    virtual ~Vehicle() = default;
};

class Car : public Vehicle
{
public:
    void move() override
    {
        cout << "Car is moving" << endl;
    }
};

class Bike : public Vehicle
{
public:
    void move() override
    {
        cout << "Bike is moving" << endl;
    }
};

int main()
{
    Vehicle* vehicles[2];
    vehicles[0] = new Car();
    vehicles[1] = new Bike();

    for(int i=0; i<2; i++)
    {
        vehicles[i]->move();
    }

    for(int i=0; i<2; i++)
    {
        delete vehicles[i];
    }

    return 0;
}