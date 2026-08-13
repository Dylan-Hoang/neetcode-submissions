# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1,head)
        curr1 = dummy
        indexgap = -1
        while indexgap < n:
            curr1 = curr1.next
            indexgap+=1
        curr2 = dummy
        while curr1:
            print(curr2.val)
            curr1 = curr1.next
            curr2 = curr2.next
        curr2.next = curr2.next.next
        return dummy.next
        