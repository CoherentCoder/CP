# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        head = ListNode()
        temp = head
        sum, carry = [], 0
        
        while True:
            _sum = l1.val + l2.val + carry
            sum.append(_sum % 10)   # reminder
            carry = _sum / 10       # carry
            if l1.next != None and l2.next != None:
                l1 = l1.next
                l2 = l2.next
            else:
                break
        
        while l1.next != None:      # l1 have some more elements
            l1 = l1.next
            _sum = l1.val + carry
            sum.append(_sum % 10)
            carry = _sum / 10
        
        while l2.next != None:      # l2 have some more elements
            l2 = l2.next
            _sum = l2.val + carry
            sum.append(_sum % 10)
            carry = _sum / 10
        
        if carry != 0:              # final carry
            sum.append(carry)
        
        for i in range(len(sum)):
            temp.val = sum[i]
            if i < len(sum)-1:
                temp.next = ListNode()
                temp = temp.next
            
        return head
