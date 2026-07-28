#include <iostream>
#include <string>

using namespace std;

class Car
{
public:
    string brand;
    int year;

    Car(string brand, int year)
    {
        this->brand = brand;
        this->year = year;
    }

    void showInfo()
    {
        cout << "Brand: " << this->brand << endl;
        cout << "Year: " << this->year << endl;
    }
};

int main()
{
    Car car("Hyundai", 2025);
    car.showInfo();
    return 0;
}