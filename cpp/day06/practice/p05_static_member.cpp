#include <iostream>
#include <string>

using namespace std;

class Car
{
public:
    string brand;

    static int carCount;

    Car(string brand)
    {
        this->brand = brand;
        carCount++;
    }

    void showInfo()
    {
        cout << "Brand: " << this->brand << endl;
    }
};

int Car::carCount = 0;

int main()
{
    Car c1("Hyundai");
    Car c2("Kia");
    Car c3("Tesla");

    cout << "Total Cars: "
         << Car::carCount << endl;

    return 0;
}