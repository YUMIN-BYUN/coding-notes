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

    Book(const Book& other)
    {
        this->price = new int(*other.price);
    }

    Book& operator=(const Book& other)
    {
        cout << "Copy Assignment" << endl;
        delete this->price;
        this->price = new int(*other.price);
        return *this;
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
    Book b2(50000);

    b2 = b1;

    *b2.price = 100000;

    b1.showInfo();
    b2.showInfo();

    return 0;
}