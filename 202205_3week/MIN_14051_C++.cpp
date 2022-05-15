#include <iostream>

using namespace std;

int n;
int maxN = 0;
int tp[15][2] = {0};

void calc(int _day, int _money)
{
	if(_day >= n)
	{
		if(maxN < _money)
		{
			maxN = _money;
		}
		
		return;
	}
	
	if(_day + tp[_day][0] <= n)
	{
		calc(_day + tp[_day][0], _money + tp[_day][1]);
	}
	
	if(_day+1 <= n)
	{
		calc(_day+1, _money);
	}
}

int main()
{
	cin >> n;
	
	for(int i = 0; i < n; i++)
	{
		cin >> tp[i][0];
		cin >> tp[i][1];
	}
	
	calc(0, 0);
	
	cout << maxN;
	
	return 0;
}
