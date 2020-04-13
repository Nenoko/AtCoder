#include <algorithm>
#include <iostream>
#include<string>
using namespace std;
int main()
{
string S;
cin>>S;
int Q;
cin>>Q;
int flipcnt=0;
int q=0;
for (int i=0;i<Q;i++){
    cin>>q;
    if (q==1){
        flipcnt += 1;
        continue;
    }
    else{
    int q2;
    char c;
    //scanf("%d %c",q2,c);
    cin>>q2>>c;
        if ((q2 + flipcnt) % 2 == 1){
            //前
            S=c+S;
        }
        else
        {
            S=S+c;
        }
    }
}
if (flipcnt % 2 == 1){
    reverse(S.begin(), S.end());
}

cout<<S<<endl;
}