"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def __init__(self):
        self.visited  = {}
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        if head in self.visited:
            return self.visited[head]
        node = Node(head.val) 
        self.visited[head] = node
        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)
        return node
        
            
            
    
    
        
        
        
        
#         if not head:
#             return
#         originalNode = head
#         copyDict = {}
#         while originalNode:
#             copyNode = Node(originalNode.val)
#             copyDict[originalNode] = copyNode
#             originalNode = originalNode.next
        
        
#         originalNode = head
#         while originalNode:
#             copyDict[originalNode].next = copyDict[originalNode.next] if originalNode.next else None
#             copyDict[originalNode].random = copyDict[originalNode.random] if originalNode.random else None
#             originalNode = originalNode.next
#         return copyDict[head]
            
            
            