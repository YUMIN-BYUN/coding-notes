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
};

void saveMovies(const vector<Movie>& movies)
{
    ofstream file("movies.txt");

    if (!file.is_open())
    {
        cout << "Failed to open file." << endl;
        return;
    }

    for (const Movie& movie : movies)
    {
        file << movie.title << " " << movie.rating << endl;
    }

    file.close();
    cout << "Movies saved successfully." << endl;
}

int main()
{
    vector<Movie> movies;
    movies.push_back(Movie("Interstellar", 9));
    movies.push_back(Movie("Inception", 8));
    movies.push_back(Movie("Tenet", 7));

    saveMovies(movies);

    return 0;
}