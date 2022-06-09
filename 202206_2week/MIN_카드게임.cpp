#include <iostream>
#include <set>


using namespace std;

int main()
{
	int n;
	cin >> n;
	
	int card1[n][5];
	int card2[n][5];
	
	for(int i = 0; i < n; i++)
	{
		cin >> card1[i][0];
		cin >> card1[i][1];
		cin >> card1[i][2];
		cin >> card1[i][3];
		cin >> card1[i][4];
	}
	
	for(int i = 0; i < n; i++)
	{
		cin >> card2[i][0];
		cin >> card2[i][1];
		cin >> card2[i][2];
		cin >> card2[i][3];
		cin >> card2[i][4];
	}
	
	int result = 0;
	
	for(int i = 0; i < n; i++)
	{
		set<int> s(card1[i], card1[i]+5);
		s.insert(card2[i][0]);
		s.insert(card2[i][1]);
		s.insert(card2[i][2]);
		s.insert(card2[i][3]);
		s.insert(card2[i][4]);
		
		if(s.size() < 10)
		{
			result++;
		}
		else
		{
			if(i > 0)
			{
				set<int> s1(card1[i-1], card1[i-1]+5);
				s1.insert(card1[i][0]);
				s1.insert(card1[i][1]);
				s1.insert(card1[i][2]);
				s1.insert(card1[i][3]);
				s1.insert(card1[i][4]);
				
				set<int> s2(card2[i-1], card2[i-1]+5);
				s2.insert(card2[i][0]);
				s2.insert(card2[i][1]);
				s2.insert(card2[i][2]);
				s2.insert(card2[i][3]);
				s2.insert(card2[i][4]);
				
				if(s1.size() < 9 || s2.size() < 9)
				{
					result++;
				}
			}
		}
	}
	
	cout << result;
	
	return 0;
}
