#include <iostream>
using namespace std;

int square(int garo, int sero, int cnt) {
    if (garo == sero) return cnt; //가로가 세로랑 같으면 이미 정사각형이므로 1 리턴

    else if (garo > sero){
        return square(garo - sero, sero, cnt + 1);
    }
    else{
        return square(garo, sero - garo, cnt + 1);
    }


}


int main(void) {
    int garo, sero; //가로 세로
    int cnt = 1;
    cin >> garo >> sero;

    cout << square(garo, sero, cnt) << endl;

    return 0;
}