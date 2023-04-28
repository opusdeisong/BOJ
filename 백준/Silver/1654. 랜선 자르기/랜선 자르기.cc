# include <iostream>
# include <algorithm>
using namespace std;

unsigned int N, K, max_temp = 0, l = 1, r = 0, m, ans = 0;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    cin >> K >> N;
    
    unsigned int* arr = new unsigned int[K];
    for (int i = 0; i < K; i ++){
        cin >> arr[i];
        max_temp = max(max_temp, arr[i]);
    }
    r = max_temp;
    while (l <= r){
        unsigned int temp = 0;
        
        m = (l + r) / 2;

        for (int i = 0; i < K; i++){
            temp += arr[i] / m;
        }

        if (temp >= N){
            l = m + 1;
            ans = max(ans, m);
        }
        else r = m - 1;

    }
    cout << ans << "\n";

}