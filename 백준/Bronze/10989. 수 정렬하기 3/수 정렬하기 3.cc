# include "iostream"

using namespace std;

int main(void){

    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N;
    cin >> N;
    int arr[10001] = {0};
    for (int i = 0; i < N; i++){
        int temp;
        cin >> temp;
        arr[temp] ++;
    }

    for (int i = 1; i <= 10000; i++){
        while(arr[i] != 0){
            cout << i << "\n";
            arr[i] --;
        }
    }
    return 0;
}