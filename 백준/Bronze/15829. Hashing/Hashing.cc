# include "iostream"
using namespace std;

int main(void){
    int N, K = 1234567891;
    long long ans = 0, temp = 0;
    string str;
    cin>>N>>str;

    for (int i = 0; i < N; i++){
        temp = str[i] - 'a' + 1;
        for (int j = 0; j < i; j++){
            temp *= 31;
            temp = temp % K;
        }
        ans += temp;
        ans = ans % K;
    }
    cout<<ans;
}