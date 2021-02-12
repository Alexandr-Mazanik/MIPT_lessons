#include <iostream>

using namespace std;

int main()
{
	int N;
	bool NisSimple = true;

	cin >> N;

	for (int i = 2; i < N; i++)
	{
		if (N % i == 0)
		{
			NisSimple = false;
			break; 
		}
	}

	NisSimple ? cout << "\n1\n" : cout << "\n0\n";

	return 0;
}