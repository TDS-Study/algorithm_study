#include <iostream>
#include <cmath>

using namespace std;

int main()
{
	int n;
	double  jimin, hansu;
	
	cin>> n >> jimin >> hansu;
	
	int cnt = 0;

	while(jimin != hansu)
	{
		jimin = round(jimin / 2);
		hansu = round(hansu / 2);

		
		cnt++;
	}
	
	cout << cnt;
	
	return 0;
	
}
