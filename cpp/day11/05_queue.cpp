#include <iostream>
#include <queue>

using namespace std;

int main()
{
    queue<int> numbers;

    numbers.push(10);
    numbers.push(20);
    numbers.push(30);

    cout << "Front : " << numbers.front() << endl;
    cout << "Back : " << numbers.back() << endl;

    numbers.pop();

    cout << "Front : " << numbers.front() << endl;

    while (!numbers.empty())
    {
        cout << numbers.front() << " ";

        numbers.pop();
    }

    cout << endl;

    return 0;
}