#include <iostream>
#include <stdexcept>


using namespace std;

void checkScore(int score)
{
    if (score < 0 || score > 100)
    {
        throw runtime_error("Score must be between 0 and 100.");
    }

    cout << "Valid score: " << score << endl;
}

int main()
{
    int score;
    cout << "Enter a score: ";
    cin >> score;

    try
    {
        checkScore(score);
    }
    catch (const exception& e)
    {
        cout << "Error: " << e.what() << endl;
    }

    return 0;
}