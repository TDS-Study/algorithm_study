/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>
#include <queue>
#include <vector>
#include <stack>
#include <string>
#include <cstring>
#include <set>
#include <unordered_set>
#include <map> 
#include <algorithm>
#include <cmath>
#define CUNLINK ios::sync_with_stdio(false), cin.tie(0), cout.tie(0)
#define ENDL cout << endl
#define ll long long
#define INF 987654321
#define Mod 10007
#define endl '\n'
#define pil pair<int,int>

using namespace std;

int main()
{
    //n 굴다리 길이
    //m 가로등 개수
    //a, b 가로등 위치
    int n, m;
    int a[100001] = {0};
    
    cin >> n >> m;
    
    /*
    if (n < m){
        return 0;
    }
    else if (a < m && b < m){
        return 0;
    }
    */
    
    //sort(a, b);
    //가로등 개수와 가로등 설치 지점 입력 받기
    for(int i = 0; i < m; i++){
        cin >> a[i];
    }
    
    int start = 0;
    int end = n;
    int result = INF;
    while(start <= end){
        //중간 값
        int mid = (start+end)/2;
        
        bool isCan = true;
        //sort(a, a+m);
        //오름차순 정렬 0번째 데이터를 중간 값과 비교
        if(a[0] > mid) isCan = false;
        //길이를 넘어 가버리는 경우에 대한 비교
        for(int i = 0; i < m-1; i++){
            if (a[i + 1] - a[i] > mid*2){
                isCan = false;
                break;
            }
        }
        if(n - a[m-1] > mid) {
            isCan = false;
        }
        //가로등 높이가 낮은 경우 +1
        if(!isCan) start = mid + 1;
        //가로등 높이가 높은 경우 -1
        //while문을 끝내기 위한 부분
        else{
            result = mid;
            end = mid -1;
        }
    }

    cout << result;
    return 0;
}
