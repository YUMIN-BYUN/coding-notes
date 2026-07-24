#include <iostream>

using namespace std;

int main()
{
    int scores[5] = {90, 85, 70, 95, 80};

    cout << "=== Original Array ===" << endl;
    cout << scores[0] << endl;
    cout << scores[1] << endl;
    cout << scores[2] << endl;
    cout << scores[3] << endl;
    cout << scores[4] << endl;

    cout << endl;

    scores[1] = 100;
    scores[3] = 60;

    cout << "=== Modified Array ===" << endl;
    cout << scores[0] << endl;
    cout << scores[1] << endl;
    cout << scores[2] << endl;
    cout << scores[3] << endl;
    cout << scores[4] << endl;

    return 0;
}