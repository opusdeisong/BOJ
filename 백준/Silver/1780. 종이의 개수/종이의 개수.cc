#include <iostream>
#include <algorithm>
using namespace std;

int N;
int arr[2188][2188], ans[3] = {0};

bool check(int r, int c, int N){
    for (int i = r; i < r + N; i++){
        for (int j = c; j < c + N; j++){
            if (arr[r][c] != arr[i][j]) return false;
        }
    }
    return true;
}

void solve(int r, int c, int N){
    if (check(r, c, N)){
        ans[arr[r][c] + 1] ++;
    }
    else{
        int temp = N / 3;
        for (int i = 0; i < 3; i++){
            for(int j = 0; j < 3; j++){
                solve(r + temp * i, c + temp * j, temp);
            }
        }
    }
}


int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    cin >> N;
    for (int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            cin >> arr[i][j];
        }
    }
    solve(0, 0, N);
    for(int i = 0; i < 3; i++){
        cout << ans[i] << "\n";
    }
    
}