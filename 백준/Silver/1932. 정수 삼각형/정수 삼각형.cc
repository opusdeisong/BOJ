#include <iostream>
#include <algorithm>
using namespace std;

int arr[500][500] = {0, };

int main(){
    int n, ans = 0;
    cin >> n;
    for (int i = 0; i < n; i++){
        for (int j = 0; j <= i; j++){
            cin >> arr[i][j];
        }
    }
    for (int i = 0; i < n; i++){
        for (int j = 0; j <= i; j++){
            if (j == 0) arr[i][j] = arr[i - 1][0] + arr[i][j];
            else if (i == j) arr[i][j] = arr[i - 1][j - 1] + arr[i][j];
            else arr[i][j] = max(arr[i - 1][j - 1] + arr[i][j], arr[i - 1][j] + arr[i][j]);

            ans = max(ans, arr[i][j]);
        }
    }
    cout << ans;
}