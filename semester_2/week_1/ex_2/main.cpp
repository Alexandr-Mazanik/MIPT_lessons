#include <iostream>
#include <math.h>

using namespace std;

int main()
{
    float leg1_len, leg2_len, hypotenuse_len;

    cout << "leg 1: ";
    cin >> leg1_len;
    cout << "leg 2: ";
    cin >> leg2_len;

    hypotenuse_len = sqrt(leg1_len*leg1_len + leg2_len*leg2_len);
    cout << "\nHypotenuse length - " << hypotenuse_len << endl;

    return 0;
}
