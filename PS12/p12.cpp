#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <cmath>

using namespace std;


int N;
int bound = 99999;
vector<vector<int> > matrix; // matrix
vector<vector<int> > priority; // matrix
vector<vector<int> > cache;
int *d; //dict of 2's multiples
int te = 0;
bool *s; //bitstring



int travel(int curr, int remain, int max) {
    if (cache[curr][remain] == 0) {
        if (find(s, s + N, 1) == s + N) {
            if (max + matrix[curr][0] < bound) {
                bound = max + matrix[curr][0];
            }

            return matrix[curr][0];
        }

        if (max > bound) {
            return 99999;
        } else {
            int min = 99999;

            for (int i = 0; i < N; i++) {
                int z = priority[curr][i];

                if (s[z]) {
                    s[z] = 0;
                    int t = travel(z, remain + d[z], max + matrix[curr][z]) + matrix[curr][z];
                    s[z] = 1;

                    if (t < min) {
                        min = t;
                        int newmax = min + max + matrix[curr][z] + t;

                        if (newmax < bound) {
                            bound = newmax;
                        }
                    }
                }
            }

            cache[curr][remain] = min;
        }
    }

    return cache[curr][remain];
}

bool Compare(int lhs, int rhs) {
    return matrix[te][lhs] < matrix[te][rhs];
}

int main() {
    cin >> N;

    matrix.resize(N);
    d = new int[N]; //dict of 2's multiples
    s = new bool[N];
    int N2 = int(pow(2.0, N + 1));
    int x = 1;
    // cout << N2 << endl;

    for (int i = 0; i < N; i++) {
        d[i] = x;
        x *= 2;
        s[i] = true;
        matrix[i].resize(N);
        vector<int> s;

        for (int j = 0; j < N; j++) {
            int a;
            cin >> a;
            matrix[i][j] = a;

            if (j != i) {
                s.push_back(j);
            }
        }

        te = i;
        sort(s.begin(), s.end(), Compare);
        priority.push_back(s);

        vector<int> m(N2, 0);
        cache.push_back(m);
    }

    s[0] = false;

    cout << travel(0, 0, 0) << endl;

    // for (int j = 0; j < N; j++) {
    //     cout << priority[0][j] << " ";
    // }
    //
    // cout << endl;
}
