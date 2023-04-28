# include "iostream"
# include "algorithm"

using namespace std;

class hello{
    public:
        string name;
        int lenOfName;
};

bool compare (hello a, hello b){
    if (a.lenOfName != b.lenOfName){
        return a.lenOfName < b.lenOfName;
    }
    else{
        return a.name < b.name;
    }
};

int main(void){
    int N;
    hello arr[25000];
    
    cin >> N;

    for (int i = 0; i < N; i++){
        cin >> arr[i].name;
        arr[i].lenOfName = arr[i].name.length();
    }
    sort(arr, arr + N, compare);
    for (int i = 0; i < N; i++){
        if (arr[i].name != arr[i + 1].name)
           cout << arr[i].name << "\n";
    }
    return 0;
}