# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []
        
        memo = {}
        
        def generate(start, end):
            if start > end:
                return [None]
            if (start, end) in memo:
                return memo[(start, end)]
            
            all_trees = []
            for i in range(start, end + 1):
                left_trees = generate(start, i - 1)
                right_trees = generate(i + 1, end)
                
                for l in left_trees:
                    for r in right_trees:
                        current_tree = TreeNode(i)
                        current_tree.left = l
                        current_tree.right = r
                        all_trees.append(current_tree)
            memo[(start, end)] = all_trees
            return all_trees
        
        return generate(1, n)
