#include <iostream>

using namespace std;

int main()
{
	int N, divider = 2;

	cin >> N;
	cout << endl;

	while (N > 1)
	{
		while (N % divider == 0)
		{
			cout << divider << endl;
			N = N / divider;
		}
		divider++;
	}

	return 0;
}