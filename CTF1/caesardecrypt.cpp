#include <bits/stdc++.h>
using namespace std;
int main()
{
    int key = 16 * 3 - 4 + 3 - 4 / 2 - 40;
    string encrypted = "890d_u890d_q8r5s_0vz88ed";
    string ans = "";
    for (char c : encrypted)
    {
        if (isdigit(c))
        {
            int temp = c - '0' - key;
            if (temp < 0)
            {
                temp += 10;
            }
            ans.push_back('0' + temp);
        }
        else if (isalpha(c))
        {
            int temp = c - 'a' - key;
            if (temp < 0)
            {
                temp += 26;
            }
            ans.push_back('a' + temp);
        }
        else
        {
            ans.push_back(c);
        }
        }
    cout << ans;
}