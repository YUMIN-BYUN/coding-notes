#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

int main()
{
    srand(time(0));
    int dice_num = rand() % 6 + 1;

    cout << "Dice: " << dice_num << endl;

    return 0;
}