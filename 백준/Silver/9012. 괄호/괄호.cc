# include <iostream>
# include <queue>
# include <string>
using namespace std;

int main(){
    int T;
    cin >>T;
    for (int i = 0; i < T; i++){
        int err = 0;
        queue<char> ans;
        string temp;
        cin >> temp;
        for (int j = 0; j < temp.length(); j++){
            if (temp[j] == '('){
                ans.push('(');
            }
            else if (!ans.empty() && temp[j] == ')'){
                ans.pop();
            }
            else {
                err++;
                break;
            }
        }
        if (!ans.empty()){
            cout << "NO" << "\n";
        }
        else if (err > 0) cout << "NO" << "\n";
        else cout << "YES" << "\n";
    }
}