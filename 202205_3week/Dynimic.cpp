#include <stdio.h>
#define max(a,b) a>b?a:b
int t[16], p[16];
int dt[16];
int main(){
	int n;
	scanf("%d",&n);
	for(int i=1;i<=n;i++){
		scanf("%d%d",&t[i],&p[i]);
	}
	for(int i=n;i>=1;i--){
		if(i+t[i]-1<=n) dt[i]=max(dt[i+1],dt[i+t[i]]+p[i]);
		else dt[i]=dt[i+1];
	}
	printf("%d",dt[1]);
}
