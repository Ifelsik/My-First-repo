#include <iostream>
using namespace std;
int main(){
	cout.setf(ios::fixed);
	cout.precision(10);
	float a,b;
	cin >> a >> b;
	long double c=a/b;
	cout << c;	
}