#include "iostream"
#include "string"
using namespace std;

int cnt = 0;

string func(string num){
    if (num.size() == 1) return num;
    else{
        int sum = 0;
        for(int i = 0; i < num.size(); i++){
            sum += num[i] - '0';//문자를 숫자로 바꾸는 편법임 다들 참고하셈
        }
        cnt ++;
        return func(to_string(sum));
    }
}

int main(void){
    string num;
    cin>>num;
    int ans;
    num = func(num);
    ans = num[0] - '0';
    cout<<cnt<<endl;
    if(ans == 3 | ans == 6 | ans ==9) cout<<"YES";
    else cout<<"NO";
}