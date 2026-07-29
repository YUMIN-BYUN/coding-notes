#include <iostream>

using namespace std;

class NumberBox
{
private:
    int* number;

public:
    NumberBox(int value)
    {
        this->number = new int(value);
        cout << "Number Acquired" << endl;
    }

    NumberBox(const NumberBox& other)
    {
        this->number = new int(*other.number);
        cout << "Number Copied" << endl;
    }

    NumberBox& operator=(const NumberBox& other)
    {
        if (this == &other)
        {
            return *this;
        }

        int* newNumber = new int(*other.number);
        delete this->number;
        this->number = newNumber;

        cout << "Number Assigned" << endl;
        return *this;
    }

    ~NumberBox()
    {
        delete this->number;
        cout << "Number Released" << endl;
    }

    void setNumber(int value)
    {
        *this->number = value;
    }

    void showInfo() const
    {
        cout << *this->number << endl;
    }
};

int main()
{
    NumberBox n1(10);
    NumberBox n2 = n1;
    NumberBox n3(30);

    n3 = n1;

    n2.setNumber(20);
    n3.setNumber(30);

    n1.showInfo();
    n2.showInfo();
    n3.showInfo();

    return 0;
}