#include <iostream>

using namespace std;

int main()
{
    int number = 10;

    auto copyLambda = [number]()
    {
        cout << "Copy: " << number << endl;
    };

    auto refLambda = [&number]()
    {
        number += 5;
        cout << "Reference: " << number << endl;
    };

    copyLambda();
    refLambda();

    cout << "Outside: " << number << endl;

    return 0;
}