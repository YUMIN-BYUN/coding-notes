#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

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
        cout << "Title: " << title << endl;
        cout << "Rating: " << rating << endl;
    }
};

void findMovie(const vector<Movie>& movies)
{
    string target;

    cout << "Enter the title of movie you want to find: ";
    cin >> target;

    auto it = find_if(
        movies.begin(),
        movies.end(),
        [&target](const Movie& movie)
        {
            return movie.title == target;
        }
    );

    if (it != movies.end())
    {
        cout << "Movie found" << endl;
        it->showInfo();
    }
    else
    {
        cout << "Movie not found" << endl;
    }
}

int main()
{
    vector<Movie> movies;

    movies.push_back(Movie("Interstellar", 9));
    movies.push_back(Movie("Inception", 8));
    movies.push_back(Movie("Tenet", 7));

    findMovie(movies);

    return 0;
}