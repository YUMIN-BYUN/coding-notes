#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
    ofstream file("data.txt");

    if (!file.is_open())
    {
        cout << "Failed to open file." << endl;
        return 1;
    }

    string name = "Alice";
    int score = 95;

    file << "Name: " << name << endl;
    file << "Score: " << score << endl;

    file.close();

    cout << "File saved successfully." << endl;

    return 0;
}