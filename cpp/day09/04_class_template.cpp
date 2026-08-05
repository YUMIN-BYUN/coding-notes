#include <iostream>

using namespace std;

template <typename T>
class Box
{
public:
    T value;

    Box(T value)
    {
        this->value = value;
    }

    void show()
    {
        cout << value << endl;
    }
};

int main()
{
    Box<int> box1(100);
    Box<double> box2(3.14);
    Box<char> box3('A');

    box1.show();
    box2.show();
    box3.show();

    return 0;
}