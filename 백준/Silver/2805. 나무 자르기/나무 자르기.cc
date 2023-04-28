# include <iostream>
# include <algorithm>
using namespace std;

long long int N, M, max_temp = 0, l = 1, r = 0, m, ans = 0;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    cin >> N >> M;
    
    long long int* arr = new long long int[N];
    for (long long int i = 0; i < N; i ++){
        cin >> arr[i];
        max_temp = max(max_temp, arr[i]);
    }
    r = max_temp;
    while (l <= r){
        long long int temp = 0;
        
        m = (l + r) / 2;

        for (long long int i = 0; i < N; i++){
            if (arr[i] > m) temp += arr[i] - m;
            }

        if (temp >= M){
            l = m + 1;
            ans = max(ans, m);
        }
        else r = m - 1;

    }
    cout << ans << "\n";

}