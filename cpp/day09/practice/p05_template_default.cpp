#include <iostream>

using namespace std;

template <typename T = double>
class Value
{
public:
    T value;

    Value(T value)
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
    Value<> v1(10);
    Value<char> v2('Z');

    v1.show();
    v2.show();

    return 0;
}