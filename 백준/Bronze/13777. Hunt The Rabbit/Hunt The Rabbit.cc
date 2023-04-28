
# include "iostream"
# include "cmath"
using namespace std;
//BOJ 13777 "Hunt the Rabbit"

int main(void){

    while (1){
        int num, min = 1, max = 50, guess = 0;
        cin>>num;
        if (num == 0){
            break;
        }
        while(1) {
            guess = (min + max) / 2;
            if (num == guess) {
                cout << guess<<endl;
                break;
            } else if (num > guess) {
                cout << guess << " ";
                min = guess + 1;
            } else if (num < guess) {
                cout << guess << " ";
                max = guess - 1;
            }
        }
    }
}