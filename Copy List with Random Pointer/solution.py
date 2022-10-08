"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        OldToCopy = {}
        OldToCopy[None] = None
        n = m = head
        while n:
            copy = Node(n.val,None,None)
            OldToCopy[n] = copy
            n = n.next
        while m:
            OldToCopy[m].next = OldToCopy[m.next]
            OldToCopy[m].random = OldToCopy[m.random]
            m = m.next                
        return OldToCopy[head]