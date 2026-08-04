#include <iostream>

using namespace std;

class Animal
{
public:
    virtual void sound()
    {
        cout << "Some sound" << endl;
    }

    virtual ~Animal() = default;
};

class Dog : public Animal
{
public:
    void sound() override
    {
        cout << "Bark!" << endl;
    }
};

class Cat : public Animal
{
public:
    void sound() override
    {
        cout << "Meow!" << endl;
    }
};

int main()
{
    Animal* animals[2];

    animals[0] = new Dog();
    animals[1] = new Cat();

    for (int i = 0; i < 2; i++)
    {
        animals[i]->sound();
    }

    for (int i = 0; i < 2; i++)
    {
        delete animals[i];
    }

    return 0;
}