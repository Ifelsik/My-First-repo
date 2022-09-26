#include <iostream>
using namespace std;
int main(){
	int a, k=0;
	long double x=1, xx;
	cin >> a;
	do {
		xx=(x+a/x)/2;
		x=xx;
		k+=1;
		} while (k!=100);
	cout << x;
}