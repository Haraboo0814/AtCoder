#include <bits/stdc++.h>
using namespace std;

int main()
{
    int N;
    cin >> N;
    vector<int> score(N);
    for (int i = 0; i < N; i++)
    {
        int s;
        cin >> s;
        score[i] = s;
    }
    int sum = 0;
    for (int i = 0; i < N; i++)
    {
        sum = sum + score[i];
    }
    int mean = sum / N;
    for (int i = 0; i < N; i++)
    {
        cout << abs(score[i] - mean) << endl;
    }
}
