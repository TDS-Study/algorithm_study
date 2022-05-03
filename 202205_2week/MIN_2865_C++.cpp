#include <iostream>
#include <algorithm>
#include <sstream>
#include <functional>
#include <cmath>

using namespace std;

int main()
{
	int n, m, k;
	
	cin >> n >> m >> k;
	cin.ignore();
	
	string str;
	int tempN;
	double tempVal;	
	double number[n+1];
	double sum = 0.0;
	
	for(int i = 0; i < n; i++)
	{
		number[i] = 0;
	}
	
	for(int i = 0; i < m; i++)
	{
		getline(cin, str);
		
		stringstream ss(str);
		ss.str(str);
		
		
		while(ss >> tempN)
		{
			ss >> tempVal;
			
			//cout << tempN << endl;
			//cout << tempVal << endl;
			
			if(number[tempN] < tempVal)
			{
				number[tempN] = tempVal;
			}
		}
	}
	
	sort(number, number+(n+1), greater<double>());
	
	for(int i = 0; i < k; i++)
	{
		//cout << number[i];
		sum += number[i];
	}
	
	cout << fixed;
	cout.precision(1);
	cout << sum;
	
	return 0;
}
