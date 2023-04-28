# include <iostream>
# include <algorithm>
using namespace std;

bool compare(int a, int b){
    return a > b;
}

int main(){
    ios_base::sync_with_stdio(false);
	cin.tie(0);

    int N, M, height;
    long long B, num;
    cin >> N >> M >> B;
    num = N * M;
    int* arr = new int[num];
    for (long long i = 0; i < num; i++){
        cin >> arr[i];
    }
    sort(arr, arr + num, compare);
    int ans = 2147483000;
    for (int i = arr[num - 1]; i <= arr[0]; i++){
        int inven = B, height_temp = i, ans_temp = 0;
        for (long long j = 0; j < num; j++){
            int temp = arr[j] - i;
            if (temp > 0){
                inven += temp;
                ans_temp += temp * 2; 
            }
            else{
                inven += temp;
                ans_temp -= temp;
            }
            if (inven < 0){
                ans_temp = 2147483000;
                break;
            }
        }
        if (ans != min(ans, ans_temp)){
            ans = ans_temp;
            height = height_temp;
        }
        if (ans == ans_temp && height != height_temp){
            height = height_temp;
        }
    }   
    cout << ans << " " << height;
}