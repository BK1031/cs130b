#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

vector<string> getElementSymbols() {
    return {
        "H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne",
        "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca",
        "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn",
        "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr", "Y", "Zr",
        "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn",
        "Sb", "Te", "I", "Xe", "Cs", "Ba", "Hf", "Ta", "W", "Re",
        "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po", "At",
        "Rn", "Fr", "Ra", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds",
        "Rg", "Cn", "Fl", "Lv", "La", "Ce", "Pr", "Nd", "Pm", "Sm",
        "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu", "Ac",
        "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es",
        "Fm", "Md", "No", "Lr"
    };
}

void toLowercase(vector<string>& elements) {
    for (auto& element : elements) {
        transform(element.begin(), element.end(), element.begin(), ::tolower);
    }
}

vector<string> getInputWords(int nWords) {
    vector<string> words(nWords);
    for (int i = 0; i < nWords; ++i) {
        cin >> words[i];
    }
    return words;
}

bool isElementSymbol(const string& word, const vector<string>& elementSymbols) {
    return find(elementSymbols.begin(), elementSymbols.end(), word) != elementSymbols.end();
}

bool isSpeakable(const string& word, const vector<string>& elementSymbols) {
    vector<bool> T(word.size() + 1, false);
    T[0] = true;

    for (size_t j = 1; j <= word.size(); ++j) {
        for (const string& symbol : elementSymbols) {
            size_t len = symbol.size();
            if (j >= len && word.substr(j - len, len) == symbol) {
                if (T[j - len]) {
                    T[j] = true;
                    break;
                }
            }
        }
    }
    return T[word.size()];
}

int main() {
    vector<string> elementSymbols = getElementSymbols();
    toLowercase(elementSymbols);

    int nWords;
    cin >> nWords;
    vector<string> words = getInputWords(nWords);

    for (const string& word : words) {
        string lowerWord = word;
        transform(lowerWord.begin(), lowerWord.end(), lowerWord.begin(), ::tolower);

        if (lowerWord.size() <= 2) {
            cout << (isElementSymbol(lowerWord, elementSymbols) ? "YES" : "NO") << endl;
        } else {
            cout << (isSpeakable(lowerWord, elementSymbols) ? "YES" : "NO") << endl;
        }
    }

    return 0;
}