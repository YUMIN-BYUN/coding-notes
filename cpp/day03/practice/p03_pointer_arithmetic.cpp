#include <iostream>

using namespace std;

int main()
{
    int data[6] = {5, 10, 15, 20, 25, 30};
    int* p = data;

    cout << *(p) << endl;
    cout << *(p+=2) << endl;
    cout << *(p-=1) << endl;

    p = data;
    for (int i=0; i<6; i++)
    {
        cout << *(p + i) << " ";
    }
    return 0;
}