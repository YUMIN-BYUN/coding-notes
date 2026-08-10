#include <iostream>
#include <stdexcept>

using namespace std;

double divide(double a, double b)
{
    if (b == 0)
    {
        throw runtime_error("Cannot divide by zero.");
    }

    return a / b;
}

int main()
{
    double a;
    double b;

    cout << "Enter two numbers: ";
    cin >> a >> b;

    try
    {
        double result = divide(a, b);

        cout << "Result: " << result << endl;
    }
    catch (const exception& e)
    {
        cout << "Error: " << e.what() << endl;
    }

    return 0;
}