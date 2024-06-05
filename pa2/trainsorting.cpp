#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int numCars;
    cin >> numCars;
    vector<int> carWeights(numCars);
    for (int i = 0; i < numCars; ++i) {
        cin >> carWeights[i];
    }

    vector<int> longestIncreasingSubsequence(numCars, 1);
    vector<int> longestDecreasingSubsequence(numCars, 1);

    int maxLength = 0;

    for (int i = numCars - 1; i >= 0; --i) {
        for (int j = numCars - 1; j > i; --j) {
            if (carWeights[j] > carWeights[i]) {
                longestIncreasingSubsequence[i] = max(longestIncreasingSubsequence[i], longestIncreasingSubsequence[j] + 1);
            }
            if (carWeights[j] < carWeights[i]) {
                longestDecreasingSubsequence[i] = max(longestDecreasingSubsequence[i], longestDecreasingSubsequence[j] + 1);
            }
        }
        maxLength = max(maxLength, longestIncreasingSubsequence[i] + longestDecreasingSubsequence[i] - 1);
    }
    cout << maxLength;

    return 0;
}