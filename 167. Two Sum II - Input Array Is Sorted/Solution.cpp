class Solution {
public:
    vector<int> twoSum(vector<int>& num, int target) {
        int l = 0,r = num.size()-1;
        while(l<r){
            int curSum = num[l]+num[r];
            if(curSum == target)
                return {l+1,r+1};
            else if(curSum > target)
                r--;
            else
                l++;
        }
        return {-1,-1};
    }   
};