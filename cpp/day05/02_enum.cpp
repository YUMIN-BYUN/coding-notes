#include <iostream>

using namespace std;

enum class Direction
{
    Left,
    Right,
    Up,
    Down
};

int main()
{
    Direction direction = Direction::Left;

    switch (direction)
    {
    case Direction::Left:
        cout << "Move Left" << endl;
        break;

    case Direction::Right:
        cout << "Move Right" << endl;
        break;

    case Direction::Up:
        cout << "Move Up" << endl;
        break;

    case Direction::Down:
        cout << "Move Down" << endl;
        break;
    }

    return 0;
}