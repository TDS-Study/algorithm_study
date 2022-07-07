#include <string>
#include <vector>
#include <queue>

using namespace std;

int count = 0;
vector<int> ex;
int _target;

void dfs(int sum, int idx)
{
    if(idx == ex.size())
    {
    	if(_target == sum)
    	{
    		count++;
		}
		
		return;
	}
	
	// 더하기 
	dfs(sum+ex[idx], idx+1);
	
	// 빼기 
	dfs(sum-ex[idx], idx+1);
}

queue<pair<int, int>> que;

int solution(vector<int> numbers, int target) {
    int answer = 0;
    //ex = numbers;
    //_target = target;
    
    
    //dfs(0, 0);
    //answer = count;
    
    // bfs
    que.push(make_pair(0, 0));
    
    while(!que.empty())
    {
        int num = que.front().first;
        int cnt = que.front().second;
        que.pop();
        
        if(numbers.size() == cnt )
        {
            if(target == num)
            {
                answer++;    
            }
        }
        else
        {
            que.push(make_pair(num + numbers[cnt], cnt + 1));
            que.push(make_pair(num - numbers[cnt], cnt + 1));
        }
    }
          
    
    
    
    return answer;
}
