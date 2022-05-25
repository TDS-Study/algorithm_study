#include <iostream>

using namespace std;

int main()
{
	int n;
	cin >> n;
	
	int sum = 0;
	int cnt = 0;
	
	while(sum < n)
	{
		cnt++;
		sum = sum + cnt;
	}
	
	sum = sum - cnt + 1;
	int diff = n - sum;
	int up;
	int down;
	
	if(cnt%2 == 0)
	{
		up = 1 + diff;
		down = cnt - diff;
	}
	else
	{
		up = cnt - diff;
		down = 1 + diff;
	}
	
	cout << up << "/" << down;
	
	
	return 0;
}
