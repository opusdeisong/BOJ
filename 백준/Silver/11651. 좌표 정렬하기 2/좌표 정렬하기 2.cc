# include "iostream"
# include "algorithm"
#include "vector"

using namespace std;



int main(void){

    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N;

    cin >> N;

    vector<vector<int> > arr(N, vector<int>(2,0));
    
    for (int i = 0; i < N; i++){
        cin >> arr[i][1] >> arr[i][0];
    }
    
    sort(arr.begin(), arr.end());
    
    for (int i = 0; i < N; i++){
        cout << arr[i][1] << " " << arr[i][0] << "\n";
    }
    return 0;
}