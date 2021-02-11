#include <iostream>

using namespace std;

int main()
{
	int element;
	int max_ch_el = 0;

	do
	{
		cin >> element;
		if (element % 2 == 0 && element > max_ch_el)
			max_ch_el = element;
	} while (element != 0);

	cout << endl << max_ch_el << endl;

	return 0;
}