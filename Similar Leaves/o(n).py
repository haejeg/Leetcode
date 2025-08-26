# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        visited = []
        leaves = []
        # print(root1)
        visited.append(root1)
        while visited:
            # print(visited)
            lastVisited = visited[len(visited) - 1]
            visited.pop(len(visited) - 1)
            if not lastVisited.left and not lastVisited.right:
                leaves.append(lastVisited.val)
            if lastVisited.right:
                visited.append(lastVisited.right)
            if lastVisited.left:
                visited.append(lastVisited.left)
                

        visited = []
        leaves2 = []
        # print(root1)
        visited.append(root2)
        while visited:
            # print(visited)
            lastVisited = visited[len(visited) - 1]
            visited.pop(len(visited) - 1)
            if not lastVisited.left and not lastVisited.right:
                leaves2.append(lastVisited.val)
            if lastVisited.right:
                visited.append(lastVisited.right)
            if lastVisited.left:
                visited.append(lastVisited.left)
            
        return leaves == leaves2