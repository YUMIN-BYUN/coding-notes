#include <iostream>
#include <string>
#include <vector>
#include <fstream>

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

void loadBooks(vector<Book>& books)
{
    ifstream file("books.txt");

    if (!file.is_open())
    {
        cout << "Failed to open file." << endl;
        return;
    }

    string title;
    int price;

    while (file >> title >> price)
    {
        books.push_back(Book(title, price));
    }

    file.close();

    cout << "Books loaded successfully." << endl;
}

void showBooks(const vector<Book>& books)
{
    for (const Book& book : books)
    {
        book.showInfo();
        cout << endl;
    }
}

int main()
{
    vector<Book> books;

    loadBooks(books);

    cout << endl;

    showBooks(books);

    return 0;
}