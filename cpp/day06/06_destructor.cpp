#include <iostream>
#include <string>

using namespace std;

class Car
{
public:
    string brand;

    Car(string brand)
    {
        this->brand = brand;
        cout << brand << " is created." << endl;
    }

    ~Car()
    {
        cout << brand << " is destroyed." << endl;
    }
};

int main()
{
    Car car("Hyundai");

    return 0;
}