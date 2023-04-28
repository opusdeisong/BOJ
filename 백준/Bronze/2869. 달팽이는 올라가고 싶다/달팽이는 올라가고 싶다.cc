# include "iostream"
using namespace std;

int main(void){
    int A, B, V;
    cin >> A >> B >> V;
    V = V - A;
    if (V % (B - A) == 0) cout << V / (A - B) + 1<< endl;
    else cout << V / (A - B) + 2<< endl;
}