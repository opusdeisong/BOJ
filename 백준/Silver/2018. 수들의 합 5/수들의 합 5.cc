#include <iostream>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N;
    cin >> N;
    int cnt = 1, s_ind = 1, e_ind = 1, sum = 1;
    while(e_ind != N){ 
        if (sum > N){
            sum -= s_ind;
            s_ind ++;
        }
        else if (sum < N){
            e_ind ++;
            sum += e_ind;
        }
        else{
            e_ind ++;
            sum += e_ind;
            cnt ++;
        }
    }
    cout << cnt;
}