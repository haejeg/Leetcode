#include <iostream>

using namespace std;

//9ms RT (47%), 8.2MB MEM (79%) 

class Solution {
public:
    bool isPalindrome(int x) {
        if (((x != 0) && (x % 10 == 0)) || x < 0) {
            return false;
        }

        if (x == 0) {
            return true;
        }

        int half = 0;
        while (x > half) {
            half = (half * 10) + (x % 10); 
            x = x/10;
        }

        return half == x || half/10 == x;
    }
};