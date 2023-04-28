#include "iostream"
using namespace std;
#define MAX_SIZE 100001

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int arr[MAX_SIZE], N, M;
    cin >> N >> M;
    cin >> arr[0];
    for (int i = 1; i < N; i++){
        cin >> arr[i];
        arr[i] = arr[i] + arr[i - 1];
    }
    for (int i = 0; i < M; i++){
        int temp1, temp2;
        cin >> temp1 >> temp2;
        if (temp1 > 1)
            cout << arr[temp2 - 1] - arr[temp1 - 2] << "\n";
        else cout << arr[temp2 - 1] << "\n";

    }

}