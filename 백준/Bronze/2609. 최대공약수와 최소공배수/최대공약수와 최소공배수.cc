# include "iostream"
using namespace std;

int Euclidean(int a, int b)
{
    int r = a % b;
    if (r == 0) {
      return b;
    }
    return Euclidean(b, r);
}

int main(void){
    int A, B, GCD = 0;
    cin >> A >> B;
    GCD = Euclidean(A, B);
    cout << GCD << endl;
    cout << A * B / GCD << endl;
}