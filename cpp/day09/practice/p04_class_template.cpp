#include <iostream>
#include <string>

using namespace std;

template <typename T>
class Data
{
public:
    T value;
    Data(T value)
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
    Data<string> data1("Physics");
    Data<double> data2(4.24);

    data1.show();
    data2.show();

    return 0;
}