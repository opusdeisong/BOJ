# include "iostream"

using namespace std;

int main(void){
    int N, K, temp = 1, tempp = 1;
    cin >> N >> K;
    for (int i = 1; i <= K; i++){
        temp *= i; 
    }
    for (int i = N; i >= N - K + 1; i --){
        tempp *= i;
    }
    cout << tempp / temp;
}