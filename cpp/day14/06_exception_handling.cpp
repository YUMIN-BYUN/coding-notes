#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <stdexcept>

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
    try
    {
        ifstream file("books.txt");

        if (!file.is_open())
        {
            throw runtime_error("Failed to open file.");
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
    catch (const exception& e)
    {
        cout << "Error: " << e.what() << endl;
    }
}

int main()
{
    vector<Book> books;

    loadBooks(books);

    return 0;
}