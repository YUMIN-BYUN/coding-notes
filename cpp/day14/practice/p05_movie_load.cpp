#include <iostream>
#include <string>
#include <vector>
#include <fstream>

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
    ifstream file("movies.txt");

    if (!file.is_open())
    {
        cout << "Failed to open file." << endl;
        return;
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

void showMovies(const vector<Movie>& movies)
{
    for(const Movie& movie : movies)
    {
        movie.showInfo();
    }
}

int main()
{
    vector<Movie> movies;

    loadMovies(movies);

    showMovies(movies);

    return 0;
}