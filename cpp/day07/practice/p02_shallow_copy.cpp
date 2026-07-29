#include <iostream>

using namespace std;

class Book
{
public:
    int* price;

    Book(int price)
    {
        this->price = new int(price);
    }

    ~Book()
    {
        delete price;
    }

    void showInfo()
    {
        cout << *this->price << endl;
    }
};

int main()
{
    Book b1(30000);

    Book b2 = b1;

    *b2.price = 50000;

    b1.showInfo();
    b2.showInfo();

    return 0;
}