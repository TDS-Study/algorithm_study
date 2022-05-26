#include<iostream>

using namespace std;

int main()
{
	int n;
	cin >> n;
	
	int jibang[n];
	int allpass = 0;
	int allsum = 0;
	
	for(int i = 0; i < n; i++)
	{
		cin >> jibang[i];
		
		if(allpass < jibang[i])
		{
			allpass = jibang[i];
		}
		
		allsum = allsum + jibang[i];
	}
	
	int start = 1;
	int end;
	cin >> end;
	
	int mid = (start+end) / 2;
	int sum = 0;
	int sanghan = 0;
	int max = end;
	
	if(allsum <= max)
	{
		sanghan = allpass;
	}
	else
	{
		while(end-start >= 0)
		{
			int temp = 0;
			
			for(int i = 0; i < n; i++)
			{
				if(jibang[i] < mid)
				{
					temp = temp + jibang[i];
				}
				else if(jibang[i] >= mid)
				{
					temp = temp + mid;
				}
				else
				{
					break;
				}
			}
			
			if(temp <= max)
			{
				sanghan = mid;
				start = mid + 1;
			}
			else if(temp > max)
			{
				end = mid - 1;
			}
			
			mid = (start+end) / 2;
		}
	}
	
	
	cout << sanghan;
	
	return 0;
}
