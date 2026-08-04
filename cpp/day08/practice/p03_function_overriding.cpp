#include <iostream>
#include <string>

using namespace std;

class Shape
{
public:
    void draw()
    {
        cout << "Drawing Shape" << endl;
    }
};

class Circle : public Shape
{
public:
    void draw()
    {
        cout << "Drawing Circle" << endl;
    }

    void showDrawing()
    {
        Shape::draw();
        draw();
    }
};

int main()
{
    Circle circle;
    circle.showDrawing();

    return 0;
}