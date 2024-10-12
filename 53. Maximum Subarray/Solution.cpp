class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int n = nums.size();
        int max = nums[0];
        int sum = 0;
        int start = 0;
        int arr_start,arr_end,i;
        for(i =0 ; i<n ;i++){
            
            if(sum == 0){
                start = i;
            }

            sum = sum + nums[i];

            if(sum > max){
                max = sum;
                arr_start = start;
                arr_end = i;
            } 

            if(sum < 0){
                sum = 0;
            }
        }

        return max;
    }
};