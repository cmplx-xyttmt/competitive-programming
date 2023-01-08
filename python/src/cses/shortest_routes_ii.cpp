#include <bits/stdc++.h>

using namespace std;

#define rep(i, a, b) for (int i = a; i < (b); ++i)

int maxN = 500;
long long maxDist = (long long) 1E18;
int n, m, q, a, b;
long long c;
vector<vector<int>> adj(maxN + 1);
vector<vector<long long>> distances(maxN + 1, vector<long long>(maxN + 1, maxDist));

int main()
{
    cin >> n >> m >> q;

    rep(i, 0, m)
    {
        cin >> a >> b >> c;
        distances[a][b] = min(distances[a][b], c);
        distances[b][a] = distances[a][b];
    }
    rep(i, 1, n + 1) {
        distances[i][i] = 0;
    }

    rep(k, 1, n + 1) {
        rep(i, 1, n + 1) {
            rep(j, 1, n + 1) {
                distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j]);
            }
        }
    }

    rep(i, 0, q) {
        cin >> a >> b;
        if(distances[a][b] == maxDist) cout << -1 << endl;
        else cout << distances[a][b] << endl;
    }
}
