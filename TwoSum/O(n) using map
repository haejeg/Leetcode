class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> map;
        for (int i = 0; i < nums.size(); i++) {
            int key = target - nums[i];
            // if not in visited list, nums[i] must be added for key comparison?
            if (map.count(key)) {
                return {i, map[key]};
            } else {
                map[nums[i]] = i;
            }
        }
        return {};
    }
};
