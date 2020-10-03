#include <bits/stdc++.h>
#include <atcoder/all>
#define rep(i, n) for (int i = 0; i < (n); ++i)
using namespace std;
using ll = long long;
using P = pair<int, int>;
using namespace atcoder;
#define REP(i, n) for ((i) = 0; (i) < (int)(n); (i)++)

int op(int a, int b)
{
    return max(a, b);
}

int e()
{
    return 0;
}

int main()
{
    int N, K, x, i, ans = 0;
    segtree<int, op, e> seg(300010);

    cin >> N >> K;

    REP(i, N)
    {
        scanf("%d", &x);
        int L = max(x - K, 0);
        int R = min(x + K, 300000);
        int tmp = seg.prod(L, R + 1) + 1;
        ans = max(ans, tmp);
        seg.set(x, tmp);
    }

    cout << ans << endl;

    return 0;
}
