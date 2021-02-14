#include <iostream>
#include <string.h>

using namespace std;

int indentical_values(string values)
{
	int num_of_ind_val;
	int max_num = 0;

	for (int i = 0; i < 3; i++){
		num_of_ind_val = 0;

		for (int j = 0; j < 3; j++){
			if (values[j] == values[i])
				num_of_ind_val++;
		}
		if (num_of_ind_val > max_num)
			max_num = num_of_ind_val;
	}

	return max_num;
}

int main()
{	
	const int max_speed = 60;
	int speed;
	string car_num;
	int money = 0;

	do{
		cin >> speed >> car_num;

		if (speed > max_speed && car_num != "A999AA")
			switch (indentical_values(car_num.substr(1, 3)))
			{
				case 2:
					money += 500;
					break;
				case 3:
					money += 1000;
					break;
				default:
					money += 100;
					break;
			}

	} while (car_num != "A999AA");

	cout << endl << money << endl;
	
	return 0;
}