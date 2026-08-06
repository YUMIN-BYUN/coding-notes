#include <iostream>
#include <queue>

using namespace std;

int main()
{
    queue<int> numbers;

    numbers.push(100);
    numbers.push(200);
    numbers.push(300);
    numbers.push(400);

    cout << numbers.front() << endl;
    cout << numbers.back() << endl;

    numbers.pop();

    while (!numbers.empty())
    {
        cout << numbers.front() << " ";

        numbers.pop();
    }

    cout << endl;

    return 0;
}