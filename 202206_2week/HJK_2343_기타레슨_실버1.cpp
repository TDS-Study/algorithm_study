#include<iostream>

using namespace std;

bool check(int m, int disc, int lec, int a[]){
	int cnt = 1, sum = 0;
	bool r = true;
	
	for(int i = 0; i < lec; i++){
		if(a[i] > m){
			r = false;
			break;			
		}

		if((a[i] + sum) > m){
			sum = a[i];
			cnt++;
		}
		else{
			sum += a[i];
		}

		if(cnt > disc)
			r = false;
			break;
	}

	return true;
}

int main()
{
	int lec, disc;
	int a[lec];	
	int sum = 0;

	cin >> lec >> disc;		

	for(int i = 0; i < lec; i++){
		cin >> a[i];		
	}

	for(int i = 0; i < lec; i++){
		sum += a[i];
	}

	cin.ignore();

	int b = 1, e = sum;
	int m = 0;
	int minVal = 1;

	for(int i = 0; i < lec; i++){
		m = (b + e) / 2;

		cout << "middle:" + to_string(m) + "\n";

		if(check(m, disc, lec, a)){
			e = m - 1;
			minVal = m;
			cout << "pass:" + to_string(m)+ " middle";
		}
		else{
			b = m + 1;
		}
	}

	cout << minVal;

	
	return 0;
}
