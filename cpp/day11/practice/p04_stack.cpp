#include <iostream>
#include <stack>

using namespace std;

int main()
{
    stack<int> numbers;
    
    numbers.push(5);
    numbers.push(10);
    numbers.push(15);
    numbers.push(20);

    cout << "Top : " << numbers.top() << endl;

    numbers.pop();
    numbers.pop();

    while (!numbers.empty())
    {
        cout << numbers.top() << " ";

        numbers.pop();
    }

    return 0;
}