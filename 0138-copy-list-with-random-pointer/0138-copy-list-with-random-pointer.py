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
        if not head:
            return
        originalNode = head
        copyDict = {}
        while originalNode:
            copyNode = Node(originalNode.val)
            copyDict[originalNode] = copyNode
            originalNode = originalNode.next
        
        
        originalNode = head
        while originalNode:
            copyDict[originalNode].next = copyDict[originalNode.next] if originalNode.next else None
            copyDict[originalNode].random = copyDict[originalNode.random] if originalNode.random else None
            originalNode = originalNode.next
        return copyDict[head]
            
            
            