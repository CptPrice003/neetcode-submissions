# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        p1 = l1
        p2 = l2
        val = 0
        carry = 0
        dummy = ListNode()
        cur = dummy

        while p1 or p2 or carry:

            val = carry
            if p1:

                val += p1.val
                p1 = p1.next

            if p2:

                val += p2.val
                p2 = p2.next

            digit = val % 10
            carry = val // 10

            cur.next = ListNode(digit)
            cur = cur.next

        return dummy.next


        