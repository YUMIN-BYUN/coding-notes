#include <iostream>
#include <string>

using namespace std;

class Vehicle
{
protected:
    string brand;

public:
    Vehicle(string brand)
    {
        this->brand = brand;
    }
};

class Car : public Vehicle
{
private:
    int year;
public:
    Car(string brand, int year)
        : Vehicle(brand)
    {
        this->year = year;
    }

    void showInfo()
    {
        cout << "Brand : " << brand << endl;
        cout << "Year : " << year << endl;
    }
};

int main()
{
    Car car("Hyundai", 2025);
    car.showInfo();
}