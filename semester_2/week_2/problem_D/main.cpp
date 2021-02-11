#include <iostream>

using namespace std;

int main()
{
	int N;

	cin >> N;

	if (N != 1){
		while (N % 2 == 0)
		N = N / 2;

		if (N == 1)
			cout << "\nYES\n";
		else
			cout << "\nNO\n";
	} 
	else
		cout << "\nNO\n";

	
	return 0;
}