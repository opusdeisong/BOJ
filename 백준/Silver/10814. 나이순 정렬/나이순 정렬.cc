# include "iostream"
# include "algorithm"

using namespace std;

class hello{
    public:
        string name;
        int age;
        int surro;
};

bool compare (hello a, hello b){
    if (a.age != b.age){
        return a.age < b.age;
    }
    else{
        return a.surro < b.surro;
    }
};

int main(void){
    int N;
    hello arr[100000];
    
    cin >> N;

    for (int i = 0; i < N; i++){
        cin >> arr[i].age >> arr[i].name;
        arr[i].surro = i;
    }
    sort(arr, arr + N, compare);
    for (int i = 0; i < N; i++){
        
       cout << arr[i].age << " " << arr[i].name << "\n";}

    return 0;
}