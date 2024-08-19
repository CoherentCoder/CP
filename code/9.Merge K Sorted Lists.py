# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    # Using simple iteration (not-optimized)
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode()   # empty linkedlist
        ptr = head          # temporary pointer (pointing to head)
        flag = True
        while flag:
            flag = False
            maxnum_index = 0
            maxnum = float('inf')
            for i in range(len(lists)):
                if lists[i] != None and lists[i].val <= maxnum:
                    maxnum_index = i
                    maxnum = lists[i].val
                    flag = True
            if flag != False and lists[maxnum_index] != None:
                lists[maxnum_index] = lists[maxnum_index].next
                ptr.next = ListNode(maxnum)
                ptr = ptr.next
        return head.next

    # Using min-heap (optimized)
    # Todo
