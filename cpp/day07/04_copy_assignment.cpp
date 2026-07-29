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
        score = new int(*other.score);
    }

    Student& operator=(const Student& other)
    {
        cout << "Copy Assignment Called" << endl;

        delete score;

        score = new int(*other.score);

        return *this;
    }

    ~Student()
    {
        delete score;
    }

    void showInfo()
    {
        cout << *score << endl;
    }
};

int main()
{
    Student s1(100);

    Student s2(200);

    s2 = s1;

    *s2.score = 999;

    s1.showInfo();

    s2.showInfo();

    return 0;
}