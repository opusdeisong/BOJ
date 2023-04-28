#include <iostream>
using namespace std;


int main() {
  while (true){
    long long a, b, c, temp = 0, ans = 0;
    cin>>a>>b>>c;
    if (a > b)
      if (a > c){
        temp = a;
        a = c;
        c = temp;
      }
    if (b > a)
      if (b > c){
        temp = b;
        b = c;
        c = temp;
      }
    if (a == 0 && b == 0 && c == 0) break;
    ans = a * a + b * b;
    if (ans == c * c) cout<<"right"<<endl;
    else cout<<"wrong"<<endl;
  }
  return 0;
}