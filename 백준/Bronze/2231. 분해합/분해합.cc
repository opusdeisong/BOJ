# include "iostream"
using namespace std;

int main(void){
    int N = 0, temp = 0,tempp = 0;
    cin>>N;
    for (int i = 0; i < N; i++){
        int ans = i;
        temp = i;tempp = i;
        while (temp > 0){
            ans += temp % 10;
            temp = temp / 10;
        }
        if (ans == N){
            cout<<i;
            break;
        }
        else tempp++;
    }
    if (tempp == N) cout<<0;
}
