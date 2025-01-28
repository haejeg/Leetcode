class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        int length = word1.length() >= word2.length() ? word1.length() : word2.length();
        string finalstr = "";
        for (int i = 0; i < length; i++) {
            if (i < word1.length()) {
                finalstr+=word1[i];
            }
            if (i < word2.length()) {
                finalstr+=word2[i];
            }
        }
        return finalstr;
    }
};