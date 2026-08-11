#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Book
{
public:
    string title;
    int price;

    Book(string title, int price)
    {
        this->title = title;
        this->price = price;
    }

    void showInfo() const
    {
        cout << "Title: " << title << endl;
        cout << "Price: " << price << endl;
    }
};

void findBook(const vector<Book>& books)
{
    string target;

    cout << "Title to find: ";
    cin >> target;

    auto it = find_if(
        books.begin(),
        books.end(),
        [&target](const Book& book)
        {
            return book.title == target;
        }
    );

    if (it != books.end())
    {
        cout << "Book found." << endl;
        it->showInfo();
    }
    else
    {
        cout << "Book not found." << endl;
    }
}

int main()
{
    vector<Book> books;

    books.push_back(Book("C++", 30000));
    books.push_back(Book("Python", 25000));
    books.push_back(Book("Physics", 40000));

    findBook(books);

    return 0;
}