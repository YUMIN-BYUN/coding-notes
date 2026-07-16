#include <iostream>

using namespace std;

int main()
{
    int score;
    do
    {
        cout << "Enter score (0 to exit): ";
        cin >> score;
        if (score != 0)
        { 
            cout << "You entered: " << score << endl;
        }
    }
    while (score != 0);
    
    cout << "Program terminated." << endl;

    return 0;
    
}