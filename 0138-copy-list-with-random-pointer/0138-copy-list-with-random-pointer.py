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
        while originalNode:
            lastNode = originalNode.next
            newNode = Node(originalNode.val)
            originalNode.next = newNode
            newNode.next = lastNode
            originalNode = lastNode
        originalNode = head
        while originalNode:
            newNode = originalNode.next
            print(originalNode.val)
            newNode.random = originalNode.random.next if  originalNode.random else None
            originalNode = newNode.next
        originalNode = head
        return_head = originalNode.next
        # return originalNode
        while originalNode:
            newNode = originalNode.next
            originalNode.next = newNode.next
            if not newNode.next:
                originalNode.next =None
                break
            originalNode = newNode.next  
            newNode.next =originalNode.next
        return return_head
        
            
            
    
    
        
        
        
        
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
            
            
            