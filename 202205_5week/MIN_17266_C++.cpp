#include<iostream>
#include<cmath>

using namespace std;

int main()
{
	int n;
	cin >> n;
	
	int m;
	cin >> m;
	
	int x[m];
	
	for(int i = 0; i < m; i++)
	{
		cin >> x[i];
	}
	
	int first;
	double mid = 0;
	int end;
	
	first = x[0];
	end = n - x[m-1];
	
	int temp = 0;
	
	for(int i = 1; i < m; i++)
	{
		temp = x[i] - x[i-1];
		
		if(mid < temp)
		{
			mid = temp;
		}
	}
	
	double h = max(first, end);
	h = max(h, round(mid / 2));
	
	cout << h;
	
	return 0;
}
