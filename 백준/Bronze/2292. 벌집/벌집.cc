# include "iostream"
using namespace std;

int main(void){
    int N, cnt = 1;
    cin >> N;
    N --;
    while (N > 0){
        if (N > cnt * 6){
            N = N - cnt * 6;
            cnt ++;
        }
        else {
            cnt ++;
            break;
        }
    }
    cout<<cnt;
}