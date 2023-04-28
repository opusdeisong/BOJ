#include <iostream>
#include <algorithm>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int N;
    cin >> N;
    long long* arr = new long long[N];
    for (int i = 0; i < N; i ++){
        cin >> arr[i];
    }
    sort(arr, arr + N);
    int M;
    cin >> M;
    for (int i = 0; i < M; i ++){
        long long temp;
        cin >> temp;
        cout << upper_bound(arr, arr + N, temp) - lower_bound(arr, arr + N, temp) << " ";
    }
}