#include <iostream>
 
using namespace std;

class Person
{
public:
    string name;
    int height;
};


int main()
{
    Person person;
    person.name = "Tom";
    person.height = 180;

    cout << "Name: " << person.name << endl;
    cout << "Height: " << person.height << " cm" << endl;

    return 0;
}