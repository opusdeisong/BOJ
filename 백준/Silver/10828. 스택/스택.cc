#include<iostream>
#include<stack>
#include<string>

using namespace std;

int main(void){
    int N, temp;
    cin >> N;
    string cmd;
    stack<int> ans;

    for(int i = 0; i < N; i++){
        cin >> cmd;
        if(cmd == "push") {
            cin>>temp;
            ans.push(temp);
        }
        else if(cmd == "size")cout<<ans.size()<<endl;
        else if(cmd == "pop") {
            if(ans.empty()) cout<<"-1"<<endl;
            else{
                cout << ans.top()<<endl;
                ans.pop();
            }
        }
        else if (cmd == "top"){
            if (ans.empty()) cout<<"-1"<<endl;
            else cout<<ans.top()<<endl;
        }
        else if (cmd == "empty"){
            if (ans.empty()) cout<<"1"<<endl;
            else cout<<"0"<<endl;
        }
    }
    return 0;
}