#include <iostream>
#include <string>

using namespace std;

class Device
{
public:
    virtual void start() = 0;
};

class Computer : public Device
{
public:
    void start() override
    {
        cout << "Computer starts" << endl;
    }
};

int main()
{
    Device* device = new Computer();
    device->start();

    delete device;
    
    return 0;
}