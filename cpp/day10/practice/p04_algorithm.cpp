#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    vector<int> numbers = {15,8,23,8,42,16,8};

    sort(numbers.begin(),numbers.end());

    for(auto const& num : numbers)
    {
        cout << num << " ";
    }

    cout<< endl;

    reverse(numbers.begin(),numbers.end());
    
    for(auto const& num : numbers)
    {
        cout << num << " ";
    }

    cout<< endl;

    auto it = find(numbers.begin(), numbers.end(), 23);

    if (it != numbers.end())
    {
        cout<< "23 Found" << endl;
    }

    cout << count(numbers.begin(), numbers.end(), 8) << endl;

    cout 
        << "Max : "
        << *max_element(numbers.begin(),numbers.end())
        << endl;

    cout 
        << "Min : "
        << *min_element(numbers.begin(),numbers.end())
        << endl;

    return 0;
}