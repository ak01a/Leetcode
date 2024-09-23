class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        std::string res = "";
        if (strs.empty()) return ""; // Handle empty input
        
        for (int i = 0; i < strs[0].size(); i++) {
            for (int j = 1; j < strs.size(); j++) { // Start from j = 1
                // Check if we've reached the end of any string or characters do not match
                if (i >= strs[j].size() || strs[j][i] != strs[0][i]) {
                    return res; // Return the current result
                }
            }
            res.push_back(strs[0][i]); // Add the character to the result
        }
        return res; // Return the longest common prefix
    }
};
