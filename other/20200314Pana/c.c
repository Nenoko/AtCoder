#include "stdio.h"

int main(void){
    long long a;
    long long b;
    long long c;

    scanf("%lld %lld %lld",&a,&b,&c);
    if (a*(a-2*b)+b*(b-2*c)+c*(c-2*a)> 0)
    {
        printf("Yes");
    }
    else
    {
        printf("No");
    }
}