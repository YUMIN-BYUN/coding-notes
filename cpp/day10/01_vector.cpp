#include <iostream>
#include <vector>

using namespace std;

int main()
{
    vector<int> numbers;

    numbers.push_back(10);
    numbers.push_back(20);
    numbers.push_back(30);

    cout << "Current size: " << numbers.size() << endl;

    cout << "Elements: ";
    for (int i = 0; i < numbers.size(); i++)
    {
        cout << numbers[i] << " ";
    }
    cout << endl;

    numbers.pop_back();

    cout << "\nAfter pop_back()" << endl;

    cout << "Current size: " << numbers.size() << endl;

    cout << "Elements: ";
    for (int i = 0; i < numbers.size(); i++)
    {
        cout << numbers[i] << " ";
    }
    cout << endl;

    numbers.clear();

    cout << "\nAfter clear()" << endl;

    if (numbers.empty())
    {
        cout << "Vector is empty." << endl;
    }

    return 0;
}