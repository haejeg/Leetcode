class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int beginningNum = 0x0;
        for (int i = 0; i < nums.size(); i++) {
            beginningNum = beginningNum^nums.at(i);
        }
        return beginningNum;
    }
};