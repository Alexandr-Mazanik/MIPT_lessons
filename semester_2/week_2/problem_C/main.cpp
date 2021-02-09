#include <iostream>

using namespace std;

int main()
{
	int num;
	int amount = 0;

	cin >> num;
	while (num != 0){
		if (num % 2 == 0)
			amount++;
		cin >> num;
	}

	cout << endl << amount << endl;

	return 0;
}