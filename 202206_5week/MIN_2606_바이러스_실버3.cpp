#include <iostream>
#include <queue>
#include <set>

using namespace std;


queue<int> que;

int main()
{
	int n;
	cin >> n;
	
	int cnt;
	cin >> cnt;
	
	set<int> node[n+1];
	
	for(int i = 0; i < cnt; i++)
	{
		int row, col;
		cin >> row >> col;
		

		node[row].insert(col);
		node[col].insert(row);

	}
	
	int count = 0;
	//cout << endl;
	
	if(cnt > 0)
	{
		bool visited[n+1] = { false };
		que.push(1);
		visited[1] = true;
		
		while(!que.empty())
		{
			int cur = que.front();
			que.pop();
			
			for (set<int>::iterator iter = node[cur].begin() ; iter != node[cur].end() ; iter++)
			{
				//cout << cur << " " << *iter << endl;
				if(!visited[*iter])
				{
					que.push(*iter);
					visited[*iter] = true;
					count++;
				}
			}
		}
	}
	
    cout << count;
	
	return 0;
}
