# include "iostream"
using namespace std;

void palindrome(int N){
    int arr[6], len = 0;
    while (N > 0){
        arr[len] = N % 10;
        len ++;
        N = N / 10;
    }
    cout << arr;
}

int main(void){
    while (true){
        int N, truth = 0;
        cin >> N;
        if (N == 0){
            break;
        }
        int arr[6], len = 0;
        while (N > 0){
            arr[len] = N % 10;
            len ++;
            N = N / 10;
        }
        len --;
        for(int i = 0; i <= len / 2; i++){
            if (arr[i] != arr[len - i]){
                cout << "no" << endl;
                break;
            }
            truth ++;
        }
        if (truth == len / 2 + 1) cout << "yes" << endl;
    }
        

}