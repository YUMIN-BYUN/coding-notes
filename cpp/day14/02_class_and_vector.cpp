#include <iostream>
#include <vector>
#include <string>

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

    void showInfo()
    {
        cout << "Title: " << title << endl;
        cout << "Price: " << price << endl;
    }
};

void addBook(vector<Book>& books)
{
    string title;
    int price;

    cout << "Title: ";
    cin >> title;

    cout << "Price: ";
    cin >> price;

    books.push_back(Book(title, price));

    cout << "Book added." << endl;
}

void showBooks(vector<Book>& books)
{
    if (books.empty())
    {
        cout << "No books." << endl;
        return;
    }

    for (Book& book : books)
    {
        book.showInfo();
        cout << endl;
    }
}

int main()
{
    vector<Book> books;

    addBook(books);
    addBook(books);

    cout << endl;

    showBooks(books);

    return 0;
}