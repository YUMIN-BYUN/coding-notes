#include <iostream>

using namespace std;

int main()
{
    int score = 80;

    auto printscore = [score]()
    {
        cout << "Score: " << score << endl;
    };

    auto plustenscore = [&score]()
    {
        score += 10;
        cout << "Updated score: " << score << endl;
    };

    printscore();
    plustenscore();

    cout << "Outside: " << score << endl;

    return 0;
}