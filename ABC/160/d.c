#include <stdio.h>
int main(void)
{
    int N,X,Y;
    scanf("%d %d %d",&N, &X, &Y);
    X -= 1;
    Y -= 1;
    int gyoretu[N][N];
    for(int i=0;i<N;i++){
        for(int j=0;j<N;j++){
            if(i==j){
                gyoretu[i][j]=0;
            }
            else if(i-j==1 || j-i==1)
            {
                gyoretu[i][j]=1;
            }
            else
            {
                gyoretu[i][j]=2000;
            }
        }
    }
    gyoretu[X][Y]=1;
    gyoretu[Y][X]=1;

    for(int k=0;k<N;k++){
        for(int i=0;i<N;i++){
            for(int j=0;j<N;j++){
                if (gyoretu[i][j]> gyoretu[i][k] + gyoretu[k][j]){
                    gyoretu[i][j] =gyoretu[i][k] + gyoretu[k][j];
                }
            }
        }
    }
    int count[N-1];
    for (int i=0;i<N;i++)
    {
        count[i]=0;
    }
    for(int i=0;i<N;i++){
        for(int j=i;j<N;j++){
            //printf("%d ",gyoretu[i][j]);
            count[gyoretu[i][j]]+=1;
        }
        //printf("\n");
    }
    for (int i=1;i<N;i++)
    {
        printf("%d\n",count[i]);
    }
    
}