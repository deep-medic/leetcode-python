# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum1 = 0
        sum2 = 0
        step1 = 0
        step2 = 0
        curr1 = l1
        curr2 = l2

        while curr1:

            sum1 += curr1.val * (10 ** step1)
            curr1 = curr1.next
            step1 += 1
            print(step1, sum1, curr1)

        while curr2:

            sum2 += curr2.val * (10 ** step2)
            curr2 = curr2.next
            step2 += 1
            print(step2, sum2, curr2)

        total = sum1 + sum2

        if total == 0:
            return ListNode(0)
        
        dummy = ListNode(None)
        cur = dummy

        while total > 0:
            cur.next = ListNode(total % 10)
            cur = cur.next
            total //= 10

        return dummy.next