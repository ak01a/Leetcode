# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def find(root,ans):
            if not root:
                return
            
            find(root.left,ans)
            find(root.right,ans)
            ans.append(root.val)

        ans = []
        find(root,ans)
        return ans
        