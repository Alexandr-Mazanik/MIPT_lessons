#include <iostream>

using namespace std;

int main()
{
    int N;
    cin >> N;

    for(int i = 0; i < N/2 + 1; i++)
    {
        for(int j = 0; j < N; j++)
            if (j < i || j >= N-i)
                cout << " ";
            else
                cout << "*";

        cout << endl;
    }

    return 0;
}
