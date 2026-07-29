#include <iostream>

using namespace std;

class Resource
{
private:
    int* data;

public:
    Resource(int value)
    {
        cout << "Resource Acquired" << endl;
        data = new int(value);
    }

    Resource(const Resource& other)
    {
        cout << "Copy Constructor Called" << endl;
        data = new int(*other.data);
    }

    Resource& operator=(const Resource& other)
    {
        cout << "Copy Assignment Called" << endl;

        if (this == &other)
        {
            return *this;
        }

        int* newData = new int(*other.data);

        delete data;

        data = newData;

        return *this;
    }

    ~Resource()
    {
        cout << "Resource Released" << endl;
        delete data;
    }

    void setValue(int value)
    {
        *data = value;
    }

    void showInfo() const
    {
        cout << "Value: " << *data << endl;
    }
};

int main()
{
    Resource r1(100);

    Resource r2 = r1;

    Resource r3(300);

    r3 = r1;

    r2.setValue(200);
    r3.setValue(300);

    r1.showInfo();
    r2.showInfo();
    r3.showInfo();

    return 0;
}