# include "iostream"
using namespace std;

int main(void){
    int N, M;
    cin>>N>>M;
    int arr[N];
    for (int i = 0; i < N; i++){
        cin>>arr[i];
    }
    int max = 0;
    for (int i = 0; i < N - 2; i++){
        for (int j = i + 1; j < N - 1; j++){
            for (int k = j + 1; k < N; k ++){
                if (arr[i] + arr[j] + arr[k] <= M){
                    if (arr[i] + arr[j] + arr[k] > max){
                        max = arr[i] + arr[j] + arr[k];
                    }
                }
            }
        }
    }
    cout<<max;

}