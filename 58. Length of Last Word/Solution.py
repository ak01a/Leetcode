class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Split the string by whitespace and remove leading/trailing whitespace
        words = s.strip().split()
        
        # If there are no words after splitting, return 0
        if not words:
            return 0
        
        # Return the length of the last word in the list of words
        return len(words[-1])

        #Mine :>
        '''
        x = s.split()
        return len(x[len(x)-1]) 
        '''