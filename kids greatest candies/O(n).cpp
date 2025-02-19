class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        vector<bool> booleans;
        int max = candies.at(0);
        for (int i = 0; i < candies.size(); i++) {
            if (candies.at(i) > max) {
                max = candies.at(i);
            }
        }

        for (int i = 0; i < candies.size(); i++) {
            booleans.push_back(max <= candies.at(i) + extraCandies);
        }

        return booleans;
    }
};