#include <iostream>

using namespace std;

class Animal
{
public:
    virtual void sound()
    {
        cout << "Some sound" << endl;
    }
};

class Dog : public Animal
{
public:
    void sound() override
    {
        cout << "Bark!" << endl;
    }
};

int main()
{
    Animal* animal = new Dog();

    animal->sound();

    delete animal;

    return 0;
}