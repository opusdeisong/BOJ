#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int N;
string arr[64];

bool check(int r, int c, int N){
    for (int i = r; i < r + N; i++){
        for (int j = c; j < c + N; j++){
            if (arr[r][c] != arr[i][j]) {
                return false;
            }
        }
    }
    return true;
}

void solve(int r, int c, int N){
    if (check(r, c, N)){
        cout << arr[r][c];
    }
    else{
        N = N / 2;
        cout << '(';
        for (int i = 0; i < 2; i ++){
            for (int j = 0; j < 2; j++){
                solve(r + N * i, c + N * j, N);
            }
        }
        cout << ')';
    }
}


int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    cin >> N;
    for (int i = 0; i < N; i++){
        cin >> arr[i];
    }
    solve(0, 0, N);
    return 0;
}