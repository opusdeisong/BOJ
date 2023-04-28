# include "iostream"
using namespace std;

int main(void){
    int T = 0;
    cin >> T;
    for(int i = 0; i < T; i ++){
        int k, n, ans[14] = {0};
        cin >> k >> n;
        for (int j = 1; j <= n; j++){
            ans[j - 1] = j;
        }//기본 케이스를 만들어주는 과정
        for (int j = 0; j < k; j++){
            for (int ii = 1; ii < n; ii++){
                ans[ii] += ans[ii - 1];
            }
        }//아래부터 위로 쭉 올라가는 과정
        cout << ans[n - 1] << endl;
    }
}