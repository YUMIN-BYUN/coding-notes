#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
    ifstream file("scores.txt");

    if (!file.is_open())
    {
        cout << "Failed to open file." << endl;
        return 1;
    }

    string name;
    int score;

    int total = 0;
    int count = 0;

    while (file >> name >> score)
    {
        cout << "Name: " << name
             << ", Score: " << score << endl;

        total += score;
        count++;
    }

    file.close();

    if (count > 0)
    {
        double average = static_cast<double>(total) / count;

        cout << "Total: " << total << endl;
        cout << "Average: " << average << endl;
    }

    return 0;
}