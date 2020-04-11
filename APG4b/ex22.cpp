#include <bits/stdc++.h>
using namespace std;
bool compare_by_b(pair<int, int> a, pair<int, int> b);

int main()
{
    int n;
    cin >> n;
    vector<pair<int, int>> v(n);
    for (int i = 0; i < n; i++)
    {
        cin >> v[i].first >> v[i].second;
    }
    sort(v.begin(), v.end(), compare_by_b);
    for (int i = 0; i < n; i++)
    {
        cout << v[i].first << ' ' << v[i].second << endl;
    }
}

bool compare_by_b(pair<int, int> a, pair<int, int> b)
{
    if (a.second != b.second)
    {
        return a.second < b.second;
    }
    else
    {
        return a.first < b.first;
    }
}
