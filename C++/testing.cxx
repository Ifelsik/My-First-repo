#include <iostream>
using namespace std;
int main()
{
	short int a;
	cin>>a;
	cout<<-((a/-1000)*1000-a%10-(((a%1000)/-100)*10+(a%100-a%10)*100));
}