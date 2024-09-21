class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        int n = nums.size();
        for(int i=0;i<n;i++){
            nums.push_back(nums[i]);
        }
        return nums;
    }
};
    //OR
    /*
        vector<int> ans;
        int n = nums.size();
        for(int i=0;i<n;i++){
            ans.push_back(nums[i]);
        }
        for(int i=0;i<n;i++){
            ans.push_back(nums[i]);
        }
        return ans;
    }

    */
