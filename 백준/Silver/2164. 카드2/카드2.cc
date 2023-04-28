# include "iostream"
# include "queue"

using namespace std;

int main(void){
    long long N;
    cin >> N;
    queue<long long> arr;
    for (int i = 1; i <= N;i ++){
        arr.push(i);
    }
    if (N != 1){
        arr.pop();
    }
    while(arr.size() != 1){
        for (int i = 0; i < 1; i++) {
            arr.push(arr.front());
            arr.pop();
        }
        arr.pop();
    }
    cout << arr.front();
}