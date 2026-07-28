#include <iostream>
#include <string>

using namespace std;

class Book
{
public:
    string title;
    int price;

    Book(string t, int p)
    {
        title = t;
        price = p;
    }

    void showInfo()
    {
        cout << "Title: " << title << endl;
        cout << "Price: " << price << endl;
    }
};

int main()
{
    Book book("C++ Programming", 30000);
    book.showInfo();

    return 0;
}