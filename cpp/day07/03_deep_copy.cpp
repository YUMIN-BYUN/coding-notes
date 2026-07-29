#include <iostream>

using namespace std;

class Student
{
public:
    int* score;

    Student(int value)
    {
        score = new int(value);
    }

    Student(const Student& other)
    {
        cout << "Deep Copy Constructor Called" << endl;
        score = new int(*other.score);
    }

    ~Student()
    {
        delete score;
    }

    void showInfo()
    {
        cout << "Score: " << *score << endl;
    }
};

int main()
{
    Student s1(100);

    Student s2 = s1;

    *s2.score = 999;

    s1.showInfo();
    s2.showInfo();

    return 0;
}