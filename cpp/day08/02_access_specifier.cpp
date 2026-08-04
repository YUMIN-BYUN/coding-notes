#include <iostream>
#include <string>

using namespace std;

class Animal
{
protected:
    string species;

public:
    Animal(string species)
    {
        this->species = species;
    }
};

class Dog : public Animal
{
private:
    string name;

public:
    Dog(string species, string name)
        : Animal(species)
    {
        this->name = name;
    }

    void showInfo()
    {
        cout << "Species : " << species << endl;
        cout << "Name : " << name << endl;
    }
};

int main()
{
    Dog dog("Dog", "Coco");

    dog.showInfo();

    return 0;
}