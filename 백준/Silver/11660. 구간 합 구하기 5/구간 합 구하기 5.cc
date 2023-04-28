#include <iostream>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int ans[1024][1024] = {0,}, N, M;
    cin >> N >> M;
    for (int i = 0; i < N; i++){
        for (int j = 0; j < N; j++){
            cin >> ans[i][j];
        }
    }
    for (int i = 0; i < N; i++){
        for (int j = 0; j < N; j++){
            if (i == 0 && j == 0)
                ans[i][j] = ans[i][j];
            else if (i == 0)
                ans[i][j] = ans[i][j - 1] + ans[i][j];
            else if (j == 0)
                ans[i][j] = ans[i - 1][j] + ans[i][j];
            else
                ans[i][j] = ans[i][j - 1] + ans[i - 1][j] - ans[i - 1][j - 1] + ans[i][j];
        }
    }
    for (int i = 0; i < M; i++){
        int temp1x, temp1y, temp2x, temp2y;
        cin >> temp1x >> temp1y >> temp2x >> temp2y;
        if (temp1x == 1 && temp1y == 1 )
            cout << ans[temp2x - 1][temp2y - 1] << "\n";
        else if (temp1x == 1)
            cout << ans[temp2x - 1][temp2y - 1] - ans[temp2x - 1][temp1y - 2]<< "\n";
        else if (temp1y == 1)
            cout << ans[temp2x - 1][temp2y - 1] - ans[temp1x - 2][temp2y - 1]<< "\n";
        else
            cout << ans[temp2x - 1][temp2y - 1] - ans[temp1x - 2][temp2y - 1] - ans[temp2x - 1][temp1y - 2] + ans[temp1x - 2][temp1y - 2] << "\n";
    }
}