#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int main()
{
    ofstream file("student.txt");
    
    if (!file.is_open())
    {
        cout << "Failed to open file." << endl;
        return 1;
    }

    string name = "Bob";
    string major = "Physics";
    int score = 88;

    file << "Name: " << name << endl;
    file << "Major: " << major << endl;
    file << "Score: " << score << endl;

    file.close();

    cout << "Student data saved " << endl;

    return 0;

}