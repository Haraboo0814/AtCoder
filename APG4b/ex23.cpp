#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin >> n;
    map<int, int> m;
    int in;
    for (int i = 0; i < n; i++)
    {
        cin >> in;
        if (m.count(in) == 0)
            m[in] = 0;
        m[in]++;
    }
    int ma = 0;
    int ans;
    for (auto p : m)
    {
        auto k = p.first;
        auto v = p.second;
        if (v > ma)
        {
            ma = v;
            ans = k;
        }
    }
    cout << ans << " " << ma << endl;
}
