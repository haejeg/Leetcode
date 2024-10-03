class Solution {
public:
    vector<int> arrayRankTransform(vector<int>& arr) {
        unordered_map<int, int> map;
        for (int i = 0; i < arr.size(); i++) {
            map[arr[i]]++;
        }
    }
};