# include "iostream"

using namespace std;

int main(void){
    long long i = 667, n, cnt = 1;
    cin >> n;

    while (true){
        if (n == 1) {
            cout << "666";
            break;
        } 
        else {
            long long temp = i, tempCnt = 0;
            while(temp > 0){
                if (temp % 10 == 6) tempCnt ++;
                else tempCnt = 0;
                if (tempCnt == 3) {
                    cnt += 1;
                    break;
                }
                temp = temp / 10;
            }
            if (cnt == n) {
                cout << i;
                break;
            }
            i ++;
        }
    }
}