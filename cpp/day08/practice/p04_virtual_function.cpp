#include <iostream>
#include <string>

using namespace std;

class Shape
{
public:
    virtual void draw()
    {
        cout << "Drawing Shape" << endl;
    }
};

class Rectangle : public Shape
{
public:
    void draw() override
    {
        cout << "Drawing Rectangle" << endl;
    }
};

int main()
{
    Shape* shape = new Rectangle();
    shape->draw();

    delete shape;

    return 0;
}