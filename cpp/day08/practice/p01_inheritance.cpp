#include <iostream>
#include <string>

using namespace std;

class Animal
{
public:
    string species;

    Animal(string species)
    {
        this->species = species;
    }

    void showSpecies()
    {
        cout << "Species : " << species << endl;
    }
};

class Dog : public Animal
{
public:
    string name;

    Dog(string species, string name)
        : Animal(species)
    {
        this->name = name;
    }

    void showInfo()
    {
        showSpecies();
        cout << "Name : " << name << endl;
    }

};

int main()
{
    Dog dog("Dog", "CoCo");
    dog.showInfo();

    return 0;
}