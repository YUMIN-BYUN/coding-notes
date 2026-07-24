#include <iostream>

using namespace std;

void changeLast(int arr[], int size)
{
    arr[size-1] = 0;
}

void addTen(int arr_1[], int size_1)
{
    for (int j = 0; j<size_1; j++)
    {
        arr_1[j] += 10;
    }
}

int main()
{
    int scores[6] = {90, 80, 70, 60, 50, 40};
    changeLast(scores,6);

    int* p = scores;

    for (int i = 0; i<6; i++)
    {
        cout << *(p+i) << " ";
    }

    cout << endl;
    
    addTen(scores,6);
    for (int k = 0; k<6; k++)
    {
        cout << *(p+k) << " ";
    }

    return 0;
}