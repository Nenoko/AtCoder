#include "stdio.h"
int main()
{
char S;
scanf("%s",S);
int Q;
scanf("%d",Q);
flipcnt=0;
int q=0;
for (int i=0;i<Q;i++){
    scanf("%d",q);
    if (q==1){
        flipcnt += 1;
        continue;
    }
    else{
    int q2;
    char c;
    scanf("%d %c",q2,c);
        if (q2 + flipcnt) % 2 == 1:
            //前
            S=c+S
        else:
            S=S+c
    }
}
if flipcnt % 2 == 1:
    S=S[::-1]

print(S)
}