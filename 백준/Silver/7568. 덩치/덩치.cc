# include "iostream"
# include "algorithm"

using namespace std;

class hello{
    public:
        int weight;
        int height;
        int cnt;
        hello() {cnt = 1;}
};


int main(void){
    int N;
    hello arr[25000];
    
    cin >> N;

    for (int i = 0; i < N; i++){
        cin >> arr[i].weight >> arr[i].height;
    }

    for (int i = 0; i < N; i++){
        for (int j = 0; j < N; j++){
            if (arr[i].weight < arr[j].weight and arr[i].height < arr[j]. height){
                arr[i].cnt ++;
            }
        }
    }

    for (int i = 0; i < N; i++){
        cout << arr[i].cnt << " ";
    }
    return 0;
}