class Solution {
public:
    vector<int> replaceElements(vector<int>& arr, int mx = -1) {
        for(int i = arr.size() - 1;i >= 0;--i)
            mx = max(mx , exchange(arr[i],mx));
        return arr;

        //Mine :>
        /* 
        int n = arr.size();
        vector<int> ans;
        for(int i =0;i<n-1;i++){
            int gr = 0;
            for(int j =i;j<n-1;j++){
                if(arr[j+1] > gr){
                    gr = arr[j+1];
                } 
            }

            ans.push_back(gr);

        }
        ans.push_back(-1);
        return ans;
        */
    }
};