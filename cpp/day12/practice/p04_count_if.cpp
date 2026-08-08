#include <algorithm>
#include <vector>
#include <iostream>

using namespace std;

int main()
{
    vector<int> scores = {95, 72, 88, 61, 100, 79, 84};

    int count = count_if(
        scores.begin(),
        scores.end(),
        [](int n)
        {
            return n >= 80;
        }
    );

    cout << "Scores above 80: " << count << endl;

    return 0;
    
}