#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <stdexcept>

using namespace std;

class Movie
{
public:
    string title;
    int rating;

    Movie(string title, int rating)
    {
        this->title = title;
        this->rating = rating;
    }

    void showInfo() const
    {
        cout << title << " " << rating << endl;
    }
};

void loadMovies(vector<Movie>& movies)
{
    try
    {
        ifstream file("movies.txt");

        if (!file.is_open())
        {
            throw runtime_error("Failed to open movies.txt");
        }

        string title;
        int rating;

        while (file >> title >> rating)
        {
            movies.push_back(Movie(title,rating));
        }

        file.close();

        cout << "Movies loaded successfully." << endl;
    }

    catch (const exception& e)
        {
            cout << "Error: " << e.what() << endl;
        }
}

int main()
{
    vector<Movie> movies;

    loadMovies(movies);

    return 0;
}