# include "iostream"
# include "algorithm"

using namespace std;

class hello{
    public:
        int x;
        int y;
};

bool compare (hello a, hello b){
    if (a.x != b.x){
        return a.x < b.x;
    }
    else{
        return a.y < b.y;
    }
};

int main(void){

    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    int N;
    hello arr[100000];
    
    cin >> N;

    for (int i = 0; i < N; i++){
        cin >> arr[i].x >> arr[i].y;
    }
    sort(arr, arr + N, compare);
    for (int i = 0; i < N; i++){
        cout << arr[i].x << " " << arr[i].y << "\n";
    }
    return 0;
}