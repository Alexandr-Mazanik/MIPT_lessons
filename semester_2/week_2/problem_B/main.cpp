#include <iostream>

using namespace std;

int main()
{
	int N;
	bool isLeapYear = false;

	cin >> N;

	if (N % 4 == 0 && N % 100 != 0 || N % 400 == 0)
		isLeapYear = true;

	if (isLeapYear)
		cout << "\nYES\n";
	else
		cout << "\nNO\n";

	return 0;
}