#include <iostream>
#include <string>

using namespace std;

class Animal
{
public:
    void sound()
    {
        cout << "Some sound" << endl;
    }
};

class Dog : public Animal
{
public:
    void sound()
    {
        Animal::sound();

        cout << "Bark!" << endl;
    }
};

int main()
{
    Dog dog;

    dog.sound();

    return 0;
}