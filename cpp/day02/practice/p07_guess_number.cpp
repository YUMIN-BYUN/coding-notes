#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

int main()
{
    srand(time(0));
    int true_num = rand() % 100 + 1;
    int input_num;

    cout << "==== Number Guessing Game ====" << endl;

    do
    {
        cout << "Guess a number (1~100): ";
        cin >> input_num;
        if (input_num > true_num)
        {
            cout << "Too high !" << endl;
        }
        else if (input_num < true_num)
        {
            cout << "Too low !" << endl;
        }
    }
    while(input_num != true_num);
    cout << "Correct!" << endl;
    cout << "Game Over." << endl;

    return 0;
}