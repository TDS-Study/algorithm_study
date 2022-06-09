#include <iostream>

using namespace std;

int main()
{
	int n, m;
	
	cin >> n >> m;
	
	int video[n];
	int end = 0;
	
	for(int i = 0; i < n; i++)
	{
		cin >> video[i];
		end = end + video[i];
	}
	
	int start = 1;
	int mid = (start + end)	/ 2;
	int min = 10000;
	
	while(end-start >= 0)
	{
		int cnt = 1;
		int temp = 0;
		
		for(int i = 0; i < n; i++)
		{
			if(mid >= temp + video[i])
			{
				temp = temp + video[i];
			}
			else if(mid < video[i])
			{
				cnt = m + 1;
				break;
			}
			else
			{
				cnt++;
				temp = video[i];
			}
			
			//cout << mid << " " << temp << " " << cnt << endl;
		}
		
		if(cnt > m)
		{
			start = mid + 1;
		}
		else if(cnt <= m)
		{
			end = mid - 1;
			min = mid;
		}

		
		mid = (start + end)	/ 2;
	}

	
	cout << min;

	return 0;
}
