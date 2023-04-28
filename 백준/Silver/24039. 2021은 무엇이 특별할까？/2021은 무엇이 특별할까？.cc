#include <iostream>
using namespace std;

int main()
{
    int arr[100] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103};
    int ans[26] = {0};
    for (int i = 0; i < 26; i++)
    {
        ans[i] = arr[i] * arr[i + 1];
    }
    int num, ans_real = 0;
    cin >> num;
    for (int i = 0; i < 26; i++)
    {
        if (num < ans[i])
        {
            ans_real = ans[i];
            break;
        }
    }
    cout << ans_real;
}