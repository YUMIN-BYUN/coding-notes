#include <iostream>

using namespace std;

void printArray(int arr[], int size)
{
    for (int i = 0; i < size; i++)
    {
        cout << arr[i] << " ";
    }

    cout << endl;
}

void changeFirst(int arr[])
{
    arr[0] = 999;
}

int main()
{
    int numbers[5] = {10, 20, 30, 40, 50};

    cout << "=== Original Array ===" << endl;
    printArray(numbers, 5);

    changeFirst(numbers);

    cout << endl;

    cout << "=== After changeFirst() ===" << endl;
    printArray(numbers, 5);

    return 0;
}