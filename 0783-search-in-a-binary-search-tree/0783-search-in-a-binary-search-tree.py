# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def helper(node : Optional[TreeNode]) -> Optional[TreeNode]:
            if node:
                if node.val == val:
                    return node 
                elif node.val < val:
                    return helper(node.right)
                else:
                    return helper(node.left)
            
            return None 
        
        return helper(root)