#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Movie
{
public:
    string title;
    int rating;

    Movie(string title, int rating)
    {
        this -> title = title;
        this -> rating = rating;
    }

    void showInfo()
    {
        cout << "Title: " << this -> title << endl;
        cout << "Rating: " << this -> rating << endl;
    }
};

void addMovie(vector<Movie>& movies)
{
    string title;
    int rating;

    cout << "Title: ";
    cin >> title;

    cout << "Rating: ";
    cin >> rating;

    movies.push_back(Movie(title, rating));
}

void showMovies(vector<Movie>& movies)
{
    if (movies.empty())
    {
        cout << "No movies" << endl;
        return;
    }
    for (Movie& movie : movies)
    {
        movie.showInfo();
        cout << endl;
    }
}

int main()
{
    vector<Movie> movies;

    addMovie(movies);
    addMovie(movies);

    cout << endl;

    showMovies(movies);

    return 0;
}
