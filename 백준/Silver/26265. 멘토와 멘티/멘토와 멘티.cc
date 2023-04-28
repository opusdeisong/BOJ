#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

bool compare(pair<string, string> &a, pair<string, string> &b){
    if (a.first == b.first){
        return a.second > b.second;
    }
    return a.first < b.first;
}


int main(){
    int N;
    cin >> N;
    vector<pair<string, string> > vec;

    for (int i = 0; i < N; i++){
        string temp1, temp2;
        cin >> temp1 >> temp2;
        vec.push_back(make_pair(temp1, temp2));
    }
    sort(vec.begin(), vec.end(), compare);
    for (int i = 0; i < N; i++){
        cout << vec[i].first <<" "<< vec[i].second << "\n";
    }
}