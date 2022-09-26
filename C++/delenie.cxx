#include <iostream>
using namespace std;
int main(){
	long double a,b;
	cin >> a >> b;
	long double c=a/b;
	int d=int(c);
	cout << d+int((c-d)/0.5);

}