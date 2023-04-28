#include<iostream>
#include<stack>
#include<string>

using namespace std;

int main(void){
    stack <char> ans;
    string temp;
    while (1){
        int k = 0;
        getline(cin, temp);
        if (temp == ".") break;
        for(int i = 0; i < temp.size(); i++){
            if (temp[i] == '(' || temp[i] == '['){
                ans.push(temp[i]);
            }
            else if (temp[i] == ')'){
                if (!ans.empty() && ans.top() == '(') ans.pop();
                else {
                    k++;
                    break;
                }
            }
            else if (temp[i] == ']'){
                if (!ans.empty() && ans.top() == '[') ans.pop();
                else {
                    k++;
                    break;
                }
            }
        }
        if (ans.empty() && k == 0){
            cout<<"yes"<<endl;
        }
        else{
            cout<<"no"<<endl;
        }
        while(!ans.empty()) ans.pop();
    }
}