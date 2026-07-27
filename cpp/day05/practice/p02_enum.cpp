#include <iostream>

using namespace std;

enum class Season
{
    Spring,
    Summer,
    Autumn,
    Winter
};

int main()
{
    Season season = Season::Summer;
    switch (season)
    {
    case Season::Spring:
        cout << "Flowers bloom." << endl;
        break;
    case Season::Summer:
        cout << "Go to the beach." << endl;
        break;
    case Season::Autumn:
        cout << "Leaves fall." << endl;
        break;
    case Season::Winter:
        cout << "Snow falls." << endl;
        break;
    }
    return 0;
}