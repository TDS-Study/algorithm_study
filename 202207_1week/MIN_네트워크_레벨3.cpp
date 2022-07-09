#include <string>
#include <vector>
#include <queue>
#include <iostream>

using namespace std;

int solution(int n, vector<vector<int>> computers) {
    int answer = 0;

    bool visited[200] = { false };
    int cnt = 0;
    queue<int> que;
    
    for(int i = 0; i < n; i++)
    {
        if(!visited[i])
        {
           // cout << computers[i][i] << ", ";
            que.push(i+1);
            visited[i] = true;
            cnt++;
            
            while(!que.empty())
            {
                int num = que.front();
                que.pop();
                
                for(int j = 0; j < n; j++)
                {
                    if(!visited[j] && computers[num-1][j] == 1)
                    {
                        cout << j+1 << ", ";
                        visited[j] = true;
                        que.push(j+1);
                    }
                }
            }
        }
        
    }
    
    
    answer = cnt;
    
    return answer;
}
