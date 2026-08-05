#include <iostream>

using namespace std;

template <typename T = int>
class Number
{
public:
    T value;

    Number(T value)
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
    Number<> n1(100);
    Number<double> n2(3.14);

    n1.show();
    n2.show();

    return 0;
}