#include <algorithm>
#include <vector>
#include <iostream>

using namespace std;


int main()
{
    vector<int> scores = {60, 70, 80, 90, 100};
    vector<int> bonusScores(scores.size());

    transform(
        scores.begin(),
        scores.end(),
        bonusScores.begin(),
        [](int n)
        {
            return n + 5;
        }
    );

    cout << "Original: ";

    for(auto const& s : scores)
    {
        cout << s << " "; 
    }

    cout << endl;

    cout << "Bonus: ";

    for(auto const& s: bonusScores)
    {
        cout << s << " ";
    }

    cout << endl;

    return 0;
}
