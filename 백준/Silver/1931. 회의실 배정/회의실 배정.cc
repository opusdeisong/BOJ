#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

bool compare(pair<int, int> a, pair<int, int> b){
    if (a.second == b.second) return a.first < b.first;
    return a.second < b.second;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N, cnt = 1;
    cin >> N;
    vector< pair<int, int> > v(N);
    for (int i = 0; i < N; i++){
        cin >> v[i].first >> v[i].second;
    }
    sort(v.begin(), v.end(), compare);
    int index = v[0].second;
    for (int i = 1; i < N; i++){
        if (index <= v[i].first){
            cnt ++;
            index = v[i].second;
        }
    }
    cout << cnt;
}