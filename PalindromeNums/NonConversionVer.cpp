#include <iostream>

using namespace std;

class Solution {
public:
    bool isPalindrome(int x) {
        if (x % 10 == 0 || x < 0) {
            return false;
        }

        int half = 0;
        while (x > half) {
            half = (half * 10) + (x % 10); 
            x = x/10;
        }
        cout<<half<<endl;
        cout<<x<<endl;
        return half == x || half/10 == x;
    }
};