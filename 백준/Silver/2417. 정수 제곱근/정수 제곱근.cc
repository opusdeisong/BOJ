# include <iostream>
# include <algorithm>
# include <cmath>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
	cin.tie(0);

    unsigned long long n;
    cin >> n;
    unsigned long long r = 3038000000;
    unsigned long long l = 1, m, ans = 1;
    while (l <= r){
        if (n == 0){
            ans = 0;
            break;
        }
        m = (l + r) / 2;
        if (m * m >= n){
            r = m - 1;
            ans = m;
        }
        else l = m + 1;
    }
    cout << ans;
}