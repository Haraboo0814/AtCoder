#include <bits/stdc++.h>
using namespace std;
int get_int();
vector<int> get_vec();
void print_vec(vector<int> vec);
int calc(int a, int b, char op);
vector<int> calc_vec(vector<int> A, vector<int> B, char op);
map<char, int> vars;
map<char, vector<int>> vecs;

int main()
{
    int n;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        string head;
        cin >> head;
        // 変数の宣言
        if (head == "int")
        {
            char name, eq;
            cin >> name >> eq;
            vars[name] = get_int();
        }
        else if (head == "print_int")
        {
            cout << get_int() << endl;
        }
        else if (head == "vec")
        {
            char name, eq;
            cin >> name >> eq;
            vecs[name] = get_vec();
        }
        else if (head == "print_vec")
        {
            print_vec(get_vec());
        }
    }
}

int get_int()
{
    int a;
    char temp;
    char op, fin;
    cin >> temp >> op;
    vector<int> ints;
    for (int i = 0; i < 10; i++)
    {
        ints.push_back(i);
    }
    a = find(ints.begin(), ints.end(), temp - '0') == ints.end() ? vars[temp] : temp - '0';
    while (op != ';')
    {
        int b;
        cin >> temp;
        b = find(ints.begin(), ints.end(), temp - '0') == ints.end() ? vars[temp] : temp - '0';
        a = calc(a, b, op);
        cin >> op;
    }
    return a;
}

vector<int> get_vec()
{
    vector<int> v;
    vector<int> ints;
    for (int i = 0; i < 10; i++)
    {
        ints.push_back(i);
    }
    char temp;
    char op;
    cin >> temp;
    if (temp != '[')
    {
        v = vecs[temp];
    }
    else
    {
        int a;
        char k;
        while (temp != ']')
        {
            cin >> k >> temp;
            a = find(ints.begin(), ints.end(), k - '0') == ints.end() ? vars[k] : k - '0';
            v.push_back(a);
        }
    }
    cin >> op;
    while (op != ';')
    {
        cin >> temp;
        vector<int> v2;
        if (op != ';')
        {
            if (temp != '[')
            {
                v2 = vecs[temp];
            }
            else
            {
                int a;
                char k;
                while (temp != ']')
                {
                    cin >> k >> temp;
                    a = find(ints.begin(), ints.end(), k - '0') == ints.end() ? vars[k] : k - '0';
                    v2.push_back(a);
                }
            }
        }
        v = calc_vec(v, v2, op);
        cin >> op;
    }
    return v;
}

// 問題文の形式でvec値を出力
void print_vec(vector<int> vec)
{
    cout << "[ ";
    for (int i = 0; i < vec.size(); i++)
    {
        cout << vec.at(i) << " ";
    }
    cout << "]" << endl;
}

// 計算
int calc(int a, int b, char op)
{
    switch (op)
    {
    case '+':
        a += b;
        break;
    case '-':
        a -= b;
        break;
    default:
        cout << "Operation error";
        exit(1);
    }
    return a;
}

vector<int> calc_vec(vector<int> A, vector<int> B, char op)
{
    for (int i = 0; i < A.size(); i++)
    {
        A[i] = op == '+' ? A[i] + B[i] : A[i] - B[i];
    }
    return A;
}