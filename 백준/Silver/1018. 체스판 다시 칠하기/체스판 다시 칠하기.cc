#include <iostream>

using namespace std;

int main(void){
    int N, M, ans = 100000;
    cin >> N >> M;
    char arr[N][M], ans1[8][8];
    ans1[0][0] = 'B';
    for (int i = 0; i < N; i++){
        for (int j = 0; j < M; j ++){
            cin >> arr[i][j];
        }
    }
    for (int i = 0; i < 8; i++){
        for (int j = 0; j < 8; j ++){
            if (i == 0 && j == 0) continue;
            else {
            if (j == 0){
                if (ans1[i - 1][j] == 'B') ans1[i][j] = 'W';
                else ans1[i][j] = 'B';
            }
            else {
                if (ans1[i][j - 1] == 'B') ans1[i][j] = 'W';
                else ans1[i][j] = 'B';
            }
            }
        }
    }
    for (int ii = 0; ii < N - 7; ii ++){
        for (int jj = 0; jj < M - 7; jj ++){
            int temp = 0;
            for (int i = 0; i < 8; i++){
                for (int j = 0; j < 8; j ++){
                    if (arr[i + ii][j + jj] != ans1[i][j]) temp ++;
                }
            }
            if (temp > 32) temp = 64 - temp;
            if (ans > temp) ans = temp;
        }
    }
    cout << ans;
}