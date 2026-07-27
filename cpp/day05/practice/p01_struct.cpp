#include <iostream>
#include <string>

using namespace std;

struct Movie
{
    string title;
    double rating;
};

Movie createMovie()
{
    Movie movie = {"Inception", 9.2};
    return movie;
}

int main()
{
    Movie movie = createMovie();
    cout << movie.title << endl;
    cout << movie.rating << endl;

    return 0;

}