#include <iostream>
#include <stack>

using namespace std;

int main()
{
    stack<int> numbers;

    numbers.push(10);
    numbers.push(20);
    numbers.push(30);

    cout << "Top : " << numbers.top() << endl;

    numbers.pop();

    cout << "Top : " << numbers.top() << endl;

    cout << "Size : " << numbers.size() << endl;

    while (!numbers.empty())
    {
        cout << numbers.top() << " ";

        numbers.pop();
    }

    cout << endl;

    return 0;
}