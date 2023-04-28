#include <iostream>
#include <algorithm>
#define MAX_SIZE 15000
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    int N, M;
    int arr[MAX_SIZE];
    cin >> N >> M;

    for(int i = 0; i < N; i++){
        cin >> arr[i];
    }
    sort(arr, arr + N);

    int s_idx = 0, e_idx = 1, cnt = 0;
    while(s_idx <= e_idx && e_idx < N){
        if(arr[s_idx] + arr[e_idx] == M) cnt ++;
        if (e_idx == N - 1){
            s_idx ++;
            e_idx = s_idx + 1;
        }
        else e_idx ++;
    }
    cout << cnt;
}