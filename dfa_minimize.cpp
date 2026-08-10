#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int c;
    if (!(cin >> c)) return 0;

    while (c--) {
        int n;
        cin >> n;

        string line;
        getline(cin, line); // consume newline

        // Read alphabet
        getline(cin, line);
        vector<char> alphabet;
        stringstream ss(line);
        char sym;
        while (ss >> sym) alphabet.push_back(sym);
        int k = alphabet.size();

        // Read final states
        getline(cin, line);
        vector<bool> is_final(n, false);
        stringstream ss2(line);
        int f;
        while (ss2 >> f) {
            if (f >= 0 && f < n) is_final[f] = true;
        }

        // Read transition table (each line: state_index followed by k destinations)
        vector<vector<int>> trans(n, vector<int>(k));
        for (int i = 0; i < n; ++i) {
            int state_idx;
            cin >> state_idx; // read and discard state index
            for (int j = 0; j < k; ++j) {
                cin >> trans[i][j];
            }
        }

        // Table-filling algorithm
        vector<vector<bool>> distinguished(n, vector<bool>(n, false));

        // Base case: mark pairs where one is final and other is not
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                if (is_final[i] != is_final[j]) {
                    distinguished[i][j] = true;
                }
            }
        }

        // Iterative marking
        bool changed = true;
        while (changed) {
            changed = false;
            for (int i = 0; i < n; ++i) {
                for (int j = i + 1; j < n; ++j) {
                    if (!distinguished[i][j]) {
                        for (int s = 0; s < k; ++s) {
                            int ni = trans[i][s];
                            int nj = trans[j][s];
                            int u = min(ni, nj);
                            int v = max(ni, nj);
                            if (u != v && distinguished[u][v]) {
                                distinguished[i][j] = true;
                                changed = true;
                                break;
                            }
                        }
                    }
                }
            }
        }

        // Collect equivalent pairs in lexicographical order
        vector<pair<int, int>> equiv;
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                if (!distinguished[i][j]) {
                    equiv.emplace_back(i, j);
                }
            }
        }

        // Output
        for (size_t i = 0; i < equiv.size(); ++i) {
            if (i) cout << ' ';
            cout << '(' << equiv[i].first << ", " << equiv[i].second << ')';
        }
        cout << '\n';
    }
    return 0;
}