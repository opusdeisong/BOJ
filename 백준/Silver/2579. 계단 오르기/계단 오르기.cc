#include <iostream>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int n;
    cin >> n;
    int* arr = new int[n];
    for (int i = 0; i < n; i++){
        cin >> arr[i];
    }
    int* ans = new int[n];
    ans[0] = arr[0];
    ans[1] = ans[0] + arr[1];
    ans[2] = max(arr[0] + arr[2], arr[1] + arr[2]);
    for (int i = 3; i < n; i++){
        ans[i] = max(ans[i - 2] + arr[i], ans[i - 3] + arr[i-1] + arr[i]);
    }
    cout << ans[n - 1];
}