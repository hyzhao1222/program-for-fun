#include <iostream>
using namespace std;
int main(){
	const double pi = 3.14159265358;
	double r1,r2,s_area,b_area,area;
	cout << "Please enter in the radius of the small circle:";
	cin >> r1;
	cout << "Please enter in the radius of the big circle:";
	cin >> r2;
	s_area = pi * r1 * r1;
	b_area = pi * r2 * r2;
	area = b_area - s_area;
	if(s_area < b_area)
		cout << "The area of the annulus is " << area;
	else
		cout << "That is not true";
	return 0;
}
// run the exe program