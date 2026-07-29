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

    ~Student()
    {
        delete score;
    }

    void show()
    {
        cout << *score << endl;
    }
};

int main()
{
    Student s1(100);

    Student s2 = s1;

    *s2.score = 999;

    s1.show();
    s2.show();

    return 0;
}