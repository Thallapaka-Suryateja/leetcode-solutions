# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None:
            return None

        seen = set()
        temp = head
        seen.add(temp.val)

        while temp.next:
            if temp.next.val in seen:
                temp.next = temp.next.next
            else:
                seen.add(temp.next.val)
                temp = temp.next

        return head