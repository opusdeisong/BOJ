# include "iostream"
# include "queue"

using namespace std;

int main(void){
    int N, K;
    cin >> N >> K;
    queue<int> arr;
    for (int i = 1; i <= N;i ++){
        arr.push(i);
    }

    cout << "<";
    while(arr.size() != 1){
        for (int i = 0; i < K - 1; i++) {
            arr.push(arr.front());
            arr.pop();
        }
        cout << arr.front() << ", ";
        arr.pop();
    }
    cout << arr.front() << ">";

}   