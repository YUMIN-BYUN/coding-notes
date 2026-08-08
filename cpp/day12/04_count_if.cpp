#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int main()
{
    vector<int> numbers = {10, 25, 7, 30, 18, 40};

    int count = count_if(
        numbers.begin(),
        numbers.end(),
        [](int n)
        {
            return n >= 20;
        }
    );

    cout << "Count: " << count << endl;

    return 0;
}