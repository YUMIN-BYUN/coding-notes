#include <iostream>

using namespace std;

int main()
{
    int num = 10;
    int other = 20;

    // 값을 수정할 수 없는 포인터
    const int* p1 = &num;
    cout << "*p1 = " << *p1 << endl;

    p1 = &other;      // 가능
    cout << "*p1 = " << *p1 << endl;

    cout << endl;

    // 포인터를 변경할 수 없는 포인터
    int* const p2 = &num;
    *p2 = 100;        // 가능
    cout << "num = " << num << endl;

    cout << endl;

    // 값도, 포인터도 변경 불가
    const int* const p3 = &num;
    cout << "*p3 = " << *p3 << endl;

    return 0;
}