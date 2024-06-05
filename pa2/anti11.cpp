#include <iostream>
#include <vector>
#include <string>
using namespace std;

const long long MOD = 1e9 + 7;
const int MAX_LENGTH = 10000;

void computeT(vector<long long>& T) {
    for (int i = 3; i <= MAX_LENGTH; i++) {
        long long result = (2 * T[i-1] - T[i-3]) % MOD;
        if (result < 0) {
            result += MOD;
        }
        T.push_back(result);
    }
}

int main() {
    vector<long long> T = {1, 2, 3};
    computeT(T);

    int n;
    cin >> n;

    vector<int> tests(n);
    for (int i = 0; i < n; i++) {
        cin >> tests[i];
    }

    for (int t : tests) {
        cout << T[t] << endl;
    }

    return 0;
}