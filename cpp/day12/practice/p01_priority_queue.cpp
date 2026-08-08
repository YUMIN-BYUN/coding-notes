#include <iostream>
#include <queue>

using namespace std;

int main()
{
    priority_queue<int> pq;

    pq.push(75);
    pq.push(92);
    pq.push(60);
    pq.push(88);
    pq.push(100);

    cout << "Highest score: " << pq.top() << endl;

    while (!pq.empty())
    {
        cout << pq.top() << " ";
        pq.pop();
    }

    return 0;
}