#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
    ofstream file("student.txt", ios::app);

    if(!file.is_open())
    {
        cout << "Failed to open file" << endl;
        return 1;
    }

    file << endl;
    
    string name = "Charlie";
    string major = "ComputerScience";
    int score = 91;

    file << "Name: " << name << endl;
    file << "Major: " << major << endl;
    file << "Score: " << score << endl;

    file.close();

    cout << "Student data appended." << endl;

    return 0;
}