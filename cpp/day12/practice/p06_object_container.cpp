#include <algorithm>
#include <vector>
#include <string>
#include <iostream>

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
};

int main()
{
    vector<Book> Books;
    Books.push_back(Book("C++ Basics", 25000));
    Books.push_back(Book("Python Guide", 18000));
    Books.push_back(Book("Algorithms", 32000));
    Books.push_back(Book("Data Science", 29000));

    auto it = find_if(
        Books.begin(),
        Books.end(),
        [](const Book& book)
        {
            return book.price >= 30000;
        }
    );

    int count = count_if(
        Books.begin(),
        Books.end(),
        [](const Book& book)
        {
            return book.price >= 25000;
        }
    );

    if (it != Books.end())
    {
        cout << "First expensive book:" << endl;
        cout << "Title: " << it->title << endl;
        cout << "Price: " << it->price << endl;
    }

    else
    {
        cout << "There is no book above 30000" << endl;
    }

    cout << "Books above 25000: " << count << endl;

    return 0;
}