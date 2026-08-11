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

void saveBooks(const vector<Book>& books)
{
    ofstream file("books.txt");

    if (!file.is_open())
    {
        cout << "Failed to open file." << endl;
        return;
    }

    for (const Book& book : books)
    {
        file << book.title << " " << book.price << endl;
    }

    file.close();

    cout << "Books saved." << endl;
}

int main()
{
    vector<Book> books;

    books.push_back(Book("C++", 30000));
    books.push_back(Book("Python", 25000));
    books.push_back(Book("Physics", 40000));

    saveBooks(books);

    return 0;
}