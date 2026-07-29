#include <iostream>
#include <string>

using namespace std;

class Book
{
public:
    string title;

    Book(string title)
    {
        this->title = title;
    }

    Book(const Book& other)
    {
        cout << "Book Copied" << endl;
        this->title = other.title;
    }

    void showInfo()
    {
        cout << "Title: " << this->title << endl;
    }
};

int main()
{
    Book book_1("C++");
    Book book_2 = book_1;
    book_2.showInfo();

    return 0;
}
