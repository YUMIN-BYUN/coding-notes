#include <iostream>
#include <string>

namespace Circle
{
    double area(double radius)
    {
        double area = 3.14 * radius * radius;
        return area;
    }
}

namespace Rectangle
{
    double area(double width, double height)
    {
        double area = width * height;
        return area;
    }
}

int main()
{
    double circleArea = Circle::area(3.0);
    double rectangleArea = Rectangle::area(4.0,5.0);
    std::cout << "Circle area : " << circleArea << std::endl;
    std::cout << "Rectangle area : " << rectangleArea << std::endl;

    return 0;
}