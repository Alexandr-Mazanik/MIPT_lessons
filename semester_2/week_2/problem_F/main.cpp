#include <iostream>

using namespace std;

int main()
{
	int element, max_el = 0;
	int num_of_max = 0;

	do
	{
		cin >> element;
		if (element > max_el)
		{
			num_of_max = 0;
			max_el = element;
		}
		if (element == max_el)
			num_of_max++;
	} while (element != 0);

	cout << endl << num_of_max << endl;

	return 0;
}