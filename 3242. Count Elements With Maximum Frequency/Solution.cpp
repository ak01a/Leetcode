class Solution {
public:
    int maxFrequencyElements(vector<int>& nums) {
        int freq[101] = {0};
        int count = 0;
        int maxF = 0;
        for(int x: nums){
            freq[x]++;
            maxF = max(freq[x],maxF);
        }
        for(int f: freq){
            if (f == maxF)
                count += maxF;
        }
        return count;
    }
};