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
        if head and head.next:
            temp=head.next
            prev=head
            while temp and temp.next:
                if temp.val==prev.val:
                    prev.next=temp.next
                    temp=prev.next
                else:
                    prev=prev.next
                    temp=temp.next
            if temp.next==None:
                if temp.val==prev.val:
                    prev.next=None
        return head


