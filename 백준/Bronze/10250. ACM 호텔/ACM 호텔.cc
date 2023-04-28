# include "iostream"
using namespace std;

int main(void){
    int T = 0;
    cin>>T;
    for (int i = 0; i < T; i++){
        int H, W, N, cnt = 1, temp = 0;
        cin>>H>>W>>N;
        cnt += N / H;
        temp = N % H;
        if (N % H == 0){
            cnt --;
            temp = H;
        }
        cout<<(temp * 100 + cnt)<<endl;
    }
}