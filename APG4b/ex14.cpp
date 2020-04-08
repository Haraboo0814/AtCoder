#include <bits/stdc++.h>
using namespace std;

int main()
{
    int A, B, C;
    cin >> A >> B >> C;
    int mi = min(min(A, B), C);
    int ma = max(max(A, B), C);
    cout << ma - mi << endl;
}
