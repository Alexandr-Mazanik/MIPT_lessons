#include <iostream>
#include <string.h>

using namespace std;

string wr_less_than_60(int number)
{
	string str;

	for (int i = 0; i < number / 10; i++)
		str.push_back('<');
	for (int i = 0; i < number % 10; i++)
		str.push_back('v');

	return str;
}

int main()
{
	int num;
	string babylon_number = "";

	cin >> num;
	int whole = num, remainder; 

	while (whole != 0)
	{
		remainder = whole % 60;
		babylon_number = wr_less_than_60(remainder) + babylon_number;

		whole = whole / 60;
		if (whole != 0)
			babylon_number = "." + babylon_number;
	}

	cout << endl << babylon_number << endl;

	return 0;
}