# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # print(lists)
        heap = []
        for i in range(len(lists)):
            if lists[i]:
                heap.append((lists[i].val,i))

        heapq.heapify(heap)
        # head = heapq.heappop(heap)
        head = current = ListNode()
        while heap:
            idx = heapq.heappop(heap)[1]
            current.next = lists[idx]
            current = current.next
            lists[idx] = lists[idx].next 
            if lists[idx]:
                heapq.heappush(heap,(lists[idx].val, idx))
        return head.next
        
#         while heap:
#             _, curr = heapq.heappop(heap)
#             head.next = curr
#             head = head.next
#         return head