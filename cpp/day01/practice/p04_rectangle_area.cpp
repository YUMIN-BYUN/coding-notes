#include <iostream>

using namespace std;

int main()
{
    double width;
    double height;

    cout << "Enter width: ";
    cin >> width;

    cout << "Enter height: ";
    cin >> height;

    cout << endl;

    cout << "Area : " << width * height << endl;
    cout << "Perimeter : " << 2 * (width + height) << endl;

    return 0;
}