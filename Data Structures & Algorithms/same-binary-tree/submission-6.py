# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if (p and not q) or (q and not p):
            return False
        
        if not p and not q:
            return True

        if p.val != q.val:
            return False

        pueue = deque()
        queue = deque()
        pueue.append(p)
        queue.append(q)

        while pueue and queue:
            curr_p = pueue.popleft()
            curr_q = queue.popleft()

            if curr_p.val != curr_q.val:
                return False
            
            if curr_p.left:
                if not curr_q.left:
                    return False
                pueue.append(curr_p.left)
            if curr_p.right:
                if not curr_q.right:
                    return False
                pueue.append(curr_p.right)
            
            if curr_q.left:
                if not curr_p.left:
                    return False
                queue.append(curr_q.left)
            if curr_q.right:
                if not curr_p.right:
                    return False
                queue.append(curr_q.right)
        
        return True



        