class Solution {
public:
    string reverseWords(string s) {
        string reversed = "";

        stringstream ss(s);

        string word;

        while (ss >> word) {
            word += ' ';
            reversed.insert(0, word);
        }

        reversed.erase(reversed.length() - 1);
        return reversed;
    }
};