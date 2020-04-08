#include <bits/stdc++.h>
using namespace std;

int main()
{
    vector<int> data(5);
    for (int i = 0; i < 5; i++)
    {
        cin >> data.at(i);
    }
    int x1 = data[0];
    for (int i = 1; i < data.size(); i++)
    {
        if (x1 == data[i])
        {
            cout << "YES" << endl;
            exit(0);
        }
        x1 = data[i];
    }
    cout << "NO" << endl;
}
