#include <iostream>

using namespace std;

class Solution {
public:
    bool isPalindrome(int x) {
        string number = to_string(x);
        for (int i = 0; i < number.length(); i++) {
            if (number[i] != number[number.length() - 1 - i]) {
                return false;
            }
        }
        return true;
    }
};