#include <iostream>

using namespace std;

int main()
{
	int num1, num2;

	cin >> num1;
	cin >> num2;
	
	if (num1 < num2){
		int buf_num = num1;
		num1 = num2;
		num2 = buf_num;
	}

	int remainder = num1 % num2;

	while (remainder != 0){
		num1 = num2;
		num2 = remainder;
		remainder = num1 % num2;
	}

	cout << endl << num2 << endl;

	return 0;
}