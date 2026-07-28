#include <iostream>
#include <string>

using namespace std;

class Dog
{
public:
    string name;
    int age;

    void bark()
    {
        cout << "Dog name: " << name << endl;
        cout << "Dog age: " << age << endl;
        cout << "Woof! Woof!" << endl;
    }
};

int main()
{
    Dog dog;
    dog.name = "Coco";
    dog.age = 3;
    dog.bark();

    return 0;
}