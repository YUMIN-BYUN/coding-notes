#include <iostream>

using namespace std;

void print (double x)
{
    cout << "Double Function" << endl;
}

template <typename T>
void print (T x)
{
    cout << "Template Function" << endl;
}

int main()
{
    print(3.14);
    print(100);
    
    return 0;
}