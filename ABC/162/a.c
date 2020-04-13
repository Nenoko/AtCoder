#include "stdio.h"
int main(void){
int N=0;
scanf("%d",&N)
int flag=1;
for(int i=0;i<3;i++)
{
    if(N==7)
    {
        flag=0;
        break;
    }
    N/=10;
}
if (flag==0){
    printf("Yes")
}else{
    printf("No")
    }
}