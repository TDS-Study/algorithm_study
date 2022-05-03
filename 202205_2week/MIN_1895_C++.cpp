#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
	int r, c = 0;
	
	cin >> r;
	cin >> c;
	
	int val[r][c];
	
	for(int i = 0; i < r; i++)
	{
		for(int j = 0; j < c; j++)
		{
			cin >> val[i][j];
		}
	}
	
	int t;
	
	cin >> t;
	
	int middle = 0;
	int result = 0;
	int sortArr[9] = {0, 0, 0, 0, 0, 0, 0, 0, 0};
	
	for(int i = 0; i < r-2; i++)
	{
		for(int j = 0; j < c-2; j++)
		{   
		    int rowcnt = 0;
		    
			for(int k = 0; k < 9; k++)
			{
//				cout << k << "/ " << i+rowcnt << "/ " << j << endl;
//				cout << val[i+rowcnt][j] << " ";
//				cout << val[i+rowcnt][j+1] << " ";
//				cout << val[i+rowcnt][j+2] << " " << endl;
				
				sortArr[k] = val[i+rowcnt][j];
				sortArr[k+1] = val[i+rowcnt][j+1];
				sortArr[k+2] = val[i+rowcnt][j+2];
				
				k += 2;
				rowcnt++;
			}

			sort(sortArr, sortArr+9);
			
			if(sortArr[4] >= t)
			{
				result++;
			}
		}
	}
	
	cout << result;
	
	return 0;
}
